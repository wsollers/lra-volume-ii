#!/usr/bin/env python3
"""Validate leaf-repo theorem/proof-stub invariants."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


PROOF_BEARING_ENVS = {"theorem", "proposition", "lemma", "corollary"}
BEGIN_ENV_RE = re.compile(
    r"\\begin\{(?P<env>theorem|proposition|lemma|corollary|definition|axiom)\}(?:\[[^\]]*\])?",
    re.DOTALL,
)
LABEL_RE = re.compile(r"\\label\{([^{}]+)\}")
PROOF_FOR_RE = re.compile(r"\\LRAProofFor\{([^{}]+)\}")
HYPERREF_RE = re.compile(r"\\hyperref\[([^\]]+)\]")
PROOF_VAULT_RE = re.compile(r"\\ProofVaultURL\{([^{}]*)\}")


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    path: str
    line: int = 1
    severity: str = "error"


@dataclass
class TheoremNode:
    env: str
    label: str | None
    path: Path
    line: int


@dataclass
class ProofFile:
    path: Path
    labels: list[str]
    proof_for: list[str]
    return_refs: list[str]
    vault_urls: list[str]
    has_professional_body: bool
    has_detailed_body: bool
    has_dependency_remark: bool


@dataclass(frozen=True)
class ProofQuality:
    score: int
    issues: list[str]


def strip_comments(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        out: list[str] = []
        escaped = False
        for ch in line:
            if ch == "\\":
                escaped = not escaped
                out.append(ch)
                continue
            if ch == "%" and not escaped:
                break
            escaped = False
            out.append(ch)
        lines.append("".join(out))
    return "\n".join(lines)


def line_number(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def is_selected_volume_part(path: Path | str, parts: set[str]) -> bool:
    path_text = path.as_posix() if isinstance(path, Path) else path.replace("\\", "/")
    return any(f"volume-ii/{part}/" in path_text for part in parts)


def iter_tex_files(root: Path, part: str) -> Iterable[Path]:
    for path in sorted(root.rglob("*.tex")):
        if any(piece.startswith(".") for piece in path.parts):
            continue
        rel_parts = path.relative_to(root).parts
        if len(rel_parts) >= 2 and rel_parts[:2] == ("archive", "legacy-orphan-proofs"):
            continue
        if part == "notes" and "proofs" in path.parts:
            continue
        if part in path.parts:
            yield path


def rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def find_matching_end(text: str, env: str, start: int) -> int:
    begin_pat = re.compile(rf"\\begin\{{{re.escape(env)}\}}")
    end_pat = re.compile(rf"\\end\{{{re.escape(env)}\}}")
    depth = 1
    pos = start
    while depth > 0:
        nb = begin_pat.search(text, pos)
        ne = end_pat.search(text, pos)
        if ne is None:
            return len(text)
        if nb is not None and nb.start() < ne.start():
            depth += 1
            pos = nb.end()
        else:
            depth -= 1
            pos = ne.end()
    return pos


def discover_theorems(root: Path, findings: list[Finding]) -> list[TheoremNode]:
    nodes: list[TheoremNode] = []
    for path in iter_tex_files(root, "notes"):
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = strip_comments(raw)
        vault_match = PROOF_VAULT_RE.search(text)
        if vault_match:
            findings.append(Finding("vault_link_in_statement", "Proof-vault backlinks belong in proof files, not theorem statement files.", rel(path, root), line_number(text, vault_match.start())))
        for match in BEGIN_ENV_RE.finditer(text):
            env = match.group("env")
            end = find_matching_end(text, env, match.end())
            body = text[match.end():end]
            labels = LABEL_RE.findall(body)
            label = labels[0] if labels else None
            line = line_number(text, match.start())
            if env in PROOF_BEARING_ENVS and not label:
                findings.append(Finding("missing_theorem_label", f"Top-level {env} has no label.", rel(path, root), line))
            nodes.append(TheoremNode(env=env, label=label, path=path, line=line))
    return nodes


def discover_proofs(root: Path) -> list[ProofFile]:
    proofs: list[ProofFile] = []
    for path in iter_tex_files(root, "proofs"):
        if path.name == "index.tex" or "exercises" in path.parts:
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = strip_comments(raw)
        labels = [label for label in LABEL_RE.findall(text) if label.startswith("prf:")]
        if not labels and not path.stem.startswith("prf-"):
            continue
        lower = text.lower()
        proofs.append(
            ProofFile(
                path=path,
                labels=labels,
                proof_for=PROOF_FOR_RE.findall(text),
                return_refs=[ref for ref in HYPERREF_RE.findall(text) if not ref.startswith("prf:")],
                vault_urls=PROOF_VAULT_RE.findall(text),
                has_professional_body=bool(re.search(r"professional\s+(standard\s+)?proof", lower)),
                has_detailed_body=bool(re.search(r"detailed\s+(learning\s+)?proof", lower)),
                has_dependency_remark=bool(re.search(r"dependenc|proof[-\s]*structure", lower)),
            )
        )
    return proofs


def proof_quality(text: str) -> ProofQuality:
    stripped = strip_comments(text)
    lower = stripped.lower()
    labels = [label for label in LABEL_RE.findall(stripped) if label.startswith("prf:")]
    proof_for = PROOF_FOR_RE.findall(stripped)
    vault_urls = PROOF_VAULT_RE.findall(stripped)
    issues: list[str] = []
    if not labels:
        issues.append("missing_proof_label")
    if not proof_for:
        issues.append("missing_lra_proof_for")
    elif len(set(proof_for)) > 1:
        issues.append("conflicting_lra_proof_for")
    if not re.search(r"professional\s+(standard\s+)?proof", lower):
        issues.append("missing_professional_body")
    if not re.search(r"detailed\s+(learning\s+)?proof", lower):
        issues.append("missing_detailed_body")
    if not re.search(r"dependenc|proof[-\s]*structure", lower):
        issues.append("missing_dependency_remark")
    if proof_for and not [ref for ref in HYPERREF_RE.findall(stripped) if not ref.startswith("prf:")]:
        issues.append("missing_return_link")
    for url in vault_urls:
        if not re.match(r"^(https?://|[A-Za-z0-9_.-]+/)", url.strip()):
            issues.append("malformed_vault_url")
    return ProofQuality(score=len(issues), issues=issues)


def count_findings(summary: dict, key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for finding in summary[key]:
        code = finding["code"]
        counts[code] = counts.get(code, 0) + 1
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def old_proofs_by_target(source_root: Path, selected_parts: set[str]) -> dict[str, list[Path]]:
    by_target: dict[str, list[Path]] = {}
    for proof in discover_proofs(source_root):
        proof_rel = rel(proof.path, source_root)
        if not is_selected_volume_part(proof_rel, selected_parts):
            continue
        for target in set(proof.proof_for):
            by_target.setdefault(target, []).append(proof.path)
    return by_target


def proof_target_counts(root: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    for proof in discover_proofs(root):
        for target in set(proof.proof_for):
            counts[target] = counts.get(target, 0) + 1
    return counts


def target_from_missing_stub(message: str) -> str | None:
    match = re.search(r"Expected proof stub for ([^.]+)\.", message)
    return match.group(1) if match else None


def repair_from_source(
    root: Path,
    source_root: Path,
    *,
    selected_parts: set[str],
    apply: bool,
    strict: bool,
    refactor_mode: bool,
) -> dict:
    before = validate(root, strict=strict, refactor_mode=refactor_mode)
    replacements: list[dict] = []
    kept: list[dict] = []

    for current in iter_tex_files(root, "proofs"):
        current_rel = rel(current, root)
        if not is_selected_volume_part(current_rel, selected_parts):
            continue
        source = source_root / current_rel
        if not source.exists() or not source.is_file():
            continue
        current_text = current.read_text(encoding="utf-8", errors="replace")
        source_text = source.read_text(encoding="utf-8", errors="replace")
        current_quality = proof_quality(current_text)
        source_quality = proof_quality(source_text)
        item = {
            "path": current_rel,
            "current_score": current_quality.score,
            "source_score": source_quality.score,
            "current_issues": current_quality.issues,
            "source_issues": source_quality.issues,
        }
        if source_quality.score < current_quality.score:
            item["action"] = "replaced" if apply else "would_replace"
            replacements.append(item)
            if apply:
                shutil.copy2(source, current)
        else:
            item["action"] = "kept"
            kept.append(item)

    after_replacements = validate(root, strict=strict, refactor_mode=refactor_mode)
    existing_targets = proof_target_counts(root)
    source_targets = old_proofs_by_target(source_root, selected_parts)
    copied_missing: list[dict] = []
    unresolved_missing: list[dict] = []

    for finding in after_replacements["errors"]:
        if finding["code"] != "missing_proof_stub":
            continue
        if not is_selected_volume_part(finding["path"], selected_parts):
            continue
        target = target_from_missing_stub(finding["message"])
        if target is None:
            unresolved_missing.append({"path": finding["path"], "line": finding["line"], "reason": "could_not_parse_target"})
            continue
        if existing_targets.get(target, 0) > 0:
            continue
        candidates = source_targets.get(target, [])
        if len(candidates) != 1:
            unresolved_missing.append(
                {
                    "target": target,
                    "path": finding["path"],
                    "line": finding["line"],
                    "reason": "source_candidate_count",
                    "source_candidate_count": len(candidates),
                }
            )
            continue
        source = candidates[0]
        source_rel = rel(source, source_root)
        destination = root / source_rel
        item = {
            "target": target,
            "source_path": source_rel,
            "destination_path": rel(destination, root),
            "action": "copied" if apply else "would_copy",
        }
        copied_missing.append(item)
        if apply:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            existing_targets[target] = existing_targets.get(target, 0) + 1

    after = validate(root, strict=strict, refactor_mode=refactor_mode)
    return {
        "root": str(root),
        "source_root": str(source_root),
        "selected_parts": sorted(selected_parts),
        "applied": apply,
        "before": {
            "status": before["status"],
            "error_count": len(before["errors"]),
            "warning_count": len(before["warnings"]),
            "errors_by_code": count_findings(before, "errors"),
            "warnings_by_code": count_findings(before, "warnings"),
        },
        "after": {
            "status": after["status"],
            "error_count": len(after["errors"]),
            "warning_count": len(after["warnings"]),
            "errors_by_code": count_findings(after, "errors"),
            "warnings_by_code": count_findings(after, "warnings"),
        },
        "proof_file_replacements": replacements,
        "proof_files_kept": kept,
        "missing_stubs_copied": copied_missing,
        "missing_stubs_unresolved": unresolved_missing,
    }


def compare_proof_files(current: Path, source: Path) -> dict:
    current_text = current.read_text(encoding="utf-8", errors="replace")
    source_text = source.read_text(encoding="utf-8", errors="replace")
    current_quality = proof_quality(current_text)
    source_quality = proof_quality(source_text)
    if source_quality.score < current_quality.score:
        recommendation = "use_source"
    elif current_quality.score < source_quality.score:
        recommendation = "keep_current"
    else:
        recommendation = "tie"
    return {
        "current": {
            "path": str(current),
            "score": current_quality.score,
            "issues": current_quality.issues,
        },
        "source": {
            "path": str(source),
            "score": source_quality.score,
            "issues": source_quality.issues,
        },
        "recommendation": recommendation,
    }


def validate(root: Path, *, strict: bool, refactor_mode: bool) -> dict:
    errors: list[Finding] = []
    warnings: list[Finding] = []
    theorems = discover_theorems(root, errors)
    proofs = discover_proofs(root)
    expected = [node for node in theorems if node.env in PROOF_BEARING_ENVS and node.label]

    theorem_labels: dict[str, list[TheoremNode]] = {}
    for node in theorems:
        if node.label:
            theorem_labels.setdefault(node.label, []).append(node)
    for label, nodes in theorem_labels.items():
        if len(nodes) > 1:
            for node in nodes:
                errors.append(Finding("duplicate_theorem_label", f"Duplicate theorem label {label}.", rel(node.path, root), node.line))

    proof_label_map: dict[str, list[ProofFile]] = {}
    proof_target_map: dict[str, list[ProofFile]] = {}
    for proof in proofs:
        proof_rel = rel(proof.path, root)
        if not proof.labels:
            errors.append(Finding("missing_proof_label", "Proof file has no prf: label.", proof_rel))
        for label in proof.labels:
            proof_label_map.setdefault(label, []).append(proof)
        if not proof.proof_for:
            errors.append(Finding("missing_lra_proof_for", "Proof file has no \\LRAProofFor{...}.", proof_rel))
        elif len(set(proof.proof_for)) > 1:
            errors.append(Finding("conflicting_lra_proof_for", f"Proof file has conflicting \\LRAProofFor targets: {', '.join(sorted(set(proof.proof_for)))}.", proof_rel))
        for target in set(proof.proof_for):
            proof_target_map.setdefault(target, []).append(proof)
            if target not in theorem_labels:
                errors.append(Finding("invalid_proof_target", f"Proof file points to nonexistent theorem label {target}.", proof_rel))
        if not proof.has_professional_body:
            errors.append(Finding("missing_professional_body", "Proof file is missing a Professional proof section/TODO.", proof_rel))
        if not proof.has_detailed_body:
            errors.append(Finding("missing_detailed_body", "Proof file is missing a Detailed learning proof section/TODO.", proof_rel))
        if not proof.has_dependency_remark:
            warnings.append(Finding("missing_dependency_remark", "Proof file has no dependency/proof-structure remark.", proof_rel, severity="warning"))
        if proof.proof_for and not proof.return_refs:
            warnings.append(Finding("missing_return_link", "Proof file has \\LRAProofFor but no theorem return hyperref.", proof_rel, severity="warning"))
        for url in proof.vault_urls:
            if not re.match(r"^(https?://|[A-Za-z0-9_.-]+/)", url.strip()):
                errors.append(Finding("malformed_vault_url", f"Malformed proof-vault backlink: {url!r}.", proof_rel))
        if "proofs" in proof.path.parts and "notes" in proof.path.parts and not refactor_mode:
            warnings.append(Finding("path_convention_mismatch", "Proof file still uses proofs/notes; future convention should mirror notes subfolders under proofs/.", proof_rel, severity="warning"))
        if not proof.vault_urls:
            warnings.append(Finding("missing_vault_backlink", "Optional proof-vault backlink is absent.", proof_rel, severity="warning"))

    for label, files in proof_label_map.items():
        if len(files) > 1:
            for proof in files:
                errors.append(Finding("duplicate_proof_label", f"Duplicate proof label {label}.", rel(proof.path, root)))

    for node in expected:
        assert node.label is not None
        matches = proof_target_map.get(node.label, [])
        if not matches:
            errors.append(Finding("missing_proof_stub", f"Expected proof stub for {node.label}.", rel(node.path, root), node.line))
        elif len(matches) > 1:
            for proof in matches:
                errors.append(Finding("multiple_proof_stubs", f"Theorem {node.label} has multiple proof stubs.", rel(proof.path, root)))

    if strict:
        optional_warning_codes = {"missing_vault_backlink", "path_convention_mismatch"}
        promoted = [warning for warning in warnings if warning.code not in optional_warning_codes]
        retained = [warning for warning in warnings if warning.code in optional_warning_codes]
        errors.extend(promoted)
        warnings = retained

    codes = [finding.code for finding in errors]
    return {
        "root": str(root),
        "theorem_count": len([node for node in theorems if node.label]),
        "expected_proof_count": len(expected),
        "proof_file_count": len(proofs),
        "missing_theorem_labels": codes.count("missing_theorem_label"),
        "missing_proof_stubs": codes.count("missing_proof_stub"),
        "duplicate_theorem_labels": codes.count("duplicate_theorem_label"),
        "duplicate_proof_labels": codes.count("duplicate_proof_label"),
        "orphan_proofs": codes.count("missing_lra_proof_for"),
        "invalid_proof_targets": codes.count("invalid_proof_target"),
        "missing_required_bodies": codes.count("missing_professional_body") + codes.count("missing_detailed_body"),
        "warnings": [asdict(warning) for warning in warnings],
        "errors": [asdict(error) for error in errors],
        "status": "PASS" if not errors else "FAIL",
    }


def print_text(summary: dict) -> None:
    print("Leaf proof validation summary")
    for key in [
        "root",
        "theorem_count",
        "expected_proof_count",
        "proof_file_count",
        "missing_theorem_labels",
        "missing_proof_stubs",
        "duplicate_theorem_labels",
        "duplicate_proof_labels",
        "orphan_proofs",
        "invalid_proof_targets",
        "missing_required_bodies",
    ]:
        print(f"{key}: {summary[key]}")
    print(f"warning_count: {len(summary['warnings'])}")
    print(f"error_count: {len(summary['errors'])}")
    print(f"status: {summary['status']}")
    for finding in summary["errors"][:50]:
        print(f"ERROR {finding['code']} {finding['path']}:{finding['line']} - {finding['message']}")
    if len(summary["errors"]) > 50:
        print(f"... {len(summary['errors']) - 50} more errors")
    for finding in summary["warnings"][:25]:
        print(f"WARN {finding['code']} {finding['path']}:{finding['line']} - {finding['message']}")
    if len(summary["warnings"]) > 25:
        print(f"... {len(summary['warnings']) - 25} more warnings")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate leaf proof-stub invariants.")
    parser.add_argument("--root", type=Path, default=Path("."), help="Leaf repo root or volume root.")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    parser.add_argument("--refactor-mode", action="store_true", help="Suppress path-layout warnings during explicit refactors.")
    parser.add_argument("--repair-from", type=Path, default=None, help="Compare proof files with a source repo and use cleaner source files.")
    parser.add_argument("--repair-parts", default="rationals,reals", help="Comma-separated Volume II parts to repair.")
    parser.add_argument("--apply-repair", action="store_true", help="Apply cleaner proof files from --repair-from.")
    parser.add_argument("--repair-report", type=Path, default=None, help="Write repair summary JSON to this path.")
    parser.add_argument("--compare-file", type=Path, default=None, help="Compare this proof file against --compare-with.")
    parser.add_argument("--compare-with", type=Path, default=None, help="Source proof file for --compare-file.")
    args = parser.parse_args(argv)

    if args.compare_file is not None or args.compare_with is not None:
        if args.compare_file is None or args.compare_with is None:
            parser.error("--compare-file and --compare-with must be used together.")
        print(json.dumps(compare_proof_files(args.compare_file.resolve(), args.compare_with.resolve()), indent=2))
        return 0

    if args.repair_from is not None:
        selected_parts = {part.strip() for part in args.repair_parts.split(",") if part.strip()}
        report = repair_from_source(
            args.root.resolve(),
            args.repair_from.resolve(),
            selected_parts=selected_parts,
            apply=args.apply_repair,
            strict=args.strict,
            refactor_mode=args.refactor_mode,
        )
        if args.repair_report is not None:
            args.repair_report.parent.mkdir(parents=True, exist_ok=True)
            args.repair_report.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report, indent=2))
        return 0 if report["after"]["status"] == "PASS" else 1

    summary = validate(args.root.resolve(), strict=args.strict, refactor_mode=args.refactor_mode)
    if args.format == "json":
        print(json.dumps(summary, indent=2))
    else:
        print_text(summary)
    return 0 if summary["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
