#!/usr/bin/env python3
"""dependency_audit.py — verify that declared dependencies are REAL.

The structural extractor (dependency_graph.py) checks that dependency edges are
well-formed (target exists, legal prefix, acyclic, reaches a root). This tool
checks something stronger and orthogonal: that every *declared* dependency is an
*actual* dependency of the thing it is attached to, and that nothing actually
used is left undeclared.

Three declared surfaces are audited:
  * theorem boxes        (notes `dependencies` block on a thm/lem/prop/cor)
  * definitions          (notes `dependencies` block on a def)
  * proof files          (`dependencies` block in the prf-*.tex via \\LRAProofFor)

Ground truth for "actually used":
  * for a definition  -> formal \\hyperref targets in the definition body
  * for a theorem     -> formal \\hyperref targets in the statement body, UNION
                         the theorem's own proof-declared dependencies, UNION any
                         declared dep whose name appears in the proof prose
  * a proof's declared deps are checked for existence (dangling) and, best-effort,
    for appearing in the proof prose.

Outputs a simple markdown report whose sections are literally the actions to take:
  ADD dep / REMOVE dep / FIX label / CREATE node / DOES-NOT-REACH-AXIOM.

Usage:
  python dependency_audit.py --repos-root . --repo-filter "lra-volume-*" \
      --root lra-volume-iii \
      --policy lra-volume-ii/docs/governance/dependency-root-policy.yaml \
      --out reports/dependency-correctness-vol-iii.md
"""
from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import dependency_graph as dg  # noqa: E402

FORMAL = re.compile(r"^(?:thm|def|lem|prop|cor|ax):")
HREF = re.compile(r"\\hyperref\[([^\]]+)\]")
DEPBLOCK = re.compile(r"\\begin\{dependencies\}(.*?)\\end\{dependencies\}", re.S)
PROOFFOR = re.compile(r"\\LRAProofFor\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
ENV_BEGIN = re.compile(r"\\begin\{(theorem|definition|lemma|proposition|corollary|axiom)\*?\}")
ENV_END = re.compile(r"\\end\{(theorem|definition|lemma|proposition|corollary|axiom)\*?\}")

_STOP = {"a", "an", "the", "of", "on", "for", "is", "at", "to", "in", "and"}


def is_formal(label: str) -> bool:
    return bool(FORMAL.match(label))


def _tok(label: str) -> set[str]:
    body = label.split(":", 1)[-1]
    return {w for w in re.split(r"[-]", body) if w and w not in _STOP}


def rename_hint(target: str, live: set[str]) -> str | None:
    """Conservative: a live label whose token set nearly matches the dangling one."""
    tt = _tok(target)
    if not tt:
        return None
    best, best_score = None, 0
    for L in live:
        lt = _tok(L)
        shared = tt & lt
        if not (tt <= lt or lt <= tt or len(shared) >= max(2, len(tt) - 1)):
            continue
        score = len(shared) - abs(len(lt) - len(tt))
        if score > best_score:
            best, best_score = L, score
    if best and best_score >= max(1, len(tt) - 1):
        return best
    return None


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def strip_dep_blocks(text: str) -> str:
    """Remove dependency blocks so their hyperrefs aren't mistaken for usage."""
    return DEPBLOCK.sub("", text)


def env_body(text: str, label: str) -> str | None:
    """Return the body of the formal environment that contains \\label{label}."""
    m = re.search(r"\\label\{" + re.escape(label) + r"\}", text)
    if not m:
        return None
    begins = [mm for mm in ENV_BEGIN.finditer(text) if mm.start() < m.start()]
    if not begins:
        return None
    start = begins[-1]
    depth = 0
    end_pos = None
    for mm in re.finditer(
        r"\\(begin|end)\{(?:theorem|definition|lemma|proposition|corollary|axiom)\*?\}",
        text[start.start():],
    ):
        if mm.group(1) == "begin":
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                end_pos = start.start() + mm.end()
                break
    if end_pos is None:
        return None
    return text[start.start():end_pos]


def _live_files(repo_root: Path) -> list[Path]:
    """Reachable ("live") .tex files only — same view the validators use."""
    from core.file_inventory import files_to_validate
    from core.volume import VOLUME_RE
    vols = [p for p in repo_root.iterdir() if p.is_dir() and VOLUME_RE.fullmatch(p.name)] or [repo_root]
    out: set[Path] = set()
    for v in vols:
        out.update(files_to_validate([v]))
    return sorted(out)


def collect_proofs(files: list[Path]) -> dict[str, dict]:
    """label -> {targets:set, lines:{target:line}, prose:str, file:str, block_line:int}."""
    proofs: dict[str, dict] = {}
    for p in files:
        if not p.name.startswith("prf-"):
            continue
        txt = p.read_text(encoding="utf-8", errors="replace")
        pf = PROOFFOR.search(txt)
        if not pf:
            continue
        owner = pf.group(1).strip()
        block = DEPBLOCK.search(txt)
        targets: set[str] = set()
        lines: dict[str, int] = {}
        block_line = 0
        if block:
            block_line = line_of(txt, block.start())
            for hm in HREF.finditer(block.group(1)):
                t = hm.group(1).strip()
                if is_formal(t):
                    targets.add(t)
                    lines.setdefault(t, block_line + block.group(1)[:hm.start()].count("\n"))
        prose = strip_dep_blocks(txt)
        entry = proofs.setdefault(owner, {"targets": set(), "lines": {}, "prose": "", "file": "", "block_line": 0})
        entry["targets"] |= targets
        entry["lines"].update(lines)
        entry["prose"] += "\n" + prose
        entry["file"] = str(p)
        entry["block_line"] = block_line
    return proofs


def _universe_edges(repos_root: Path, universe, root_repo: str):
    """Union dependency edges across EVERY repo in the universe.

    The reachability closure must be able to walk a chain that leaves the audited
    volume (e.g. vol-iii def -> vol-ii Peano/order -> ... -> ax:*). Extracting
    edges only from the root repo makes every cross-volume target look like a
    terminal leaf, so any correct chain that exits the volume is wrongly reported
    as "does not reach an axiom". Here every repo's edges are extracted (targets
    still resolve against the full universe) and unioned into one adjacency.

    Returns (root_report, all_edges): the root-only EdgeReport that still drives
    the declared-vs-used surfaces (sections 1-4), and the unioned edge list used
    only for the reachability closure.
    """
    all_edges: list = []
    root_report = None
    for repo_name in universe.repos:
        rep = dg.extract_edges_from_universe((repos_root / repo_name).resolve(), universe)
        all_edges.extend(rep.edges)
        if repo_name == root_repo:
            root_report = rep
    if root_report is None:  # root not matched by --repo-filter; extract it explicitly
        root_report = dg.extract_edges_from_universe((repos_root / root_repo).resolve(), universe)
        all_edges.extend(root_report.edges)
    return root_report, all_edges


def build(repos_root: Path, repo_filter: str, root_repo: str, policy_path: Path | None,
          closure_scope: str = "universe"):
    dg.active_tex_files = _live_files  # audit the live graph, not orphaned files
    universe = dg.build_universe(repos_root, repo_filter)
    live = {n.label for n in universe.nodes}
    node_by_label = {n.label: n for n in universe.nodes}
    root = (repos_root / root_repo).resolve()
    root_report, all_edges = _universe_edges(repos_root, universe, root_repo)
    policy = dg.load_policy(policy_path)
    if closure_scope == "universe":
        # Adjacency spans the whole universe; the *reported* scope stays pinned to
        # the root repo (validate_graph keys scope off edge_report.repo), and the
        # root's own declarations drive the missing-declaration skip logic.
        closure_report = dg.EdgeReport(
            root=str(root), repo=root_repo, universe="",
            edges=all_edges,
            declarations=root_report.declarations,
            issues=root_report.issues,
        )
    else:  # "root": legacy single-volume closure, kept for A/B comparison
        closure_report = root_report
    issues = dg.validate_graph(universe, closure_report, policy)
    files = dg.active_tex_files(root)
    # root_report (root-sourced edges only) feeds the declared-vs-used surfaces;
    # `issues` carries the no-axiom closure computed at the requested scope.
    return universe, live, node_by_label, root_report, issues, files


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos-root", default=".")
    ap.add_argument("--repo-filter", default="lra-volume-*")
    ap.add_argument("--root", required=True, help="repo whose nodes are audited, e.g. lra-volume-iii")
    ap.add_argument("--policy", default=None)
    ap.add_argument("--out", required=True)
    ap.add_argument("--closure-scope", choices=["universe", "root"], default="universe",
                    help="reachability closure: 'universe' walks edges across all repos "
                         "(true cross-volume axiom reachability); 'root' is the legacy "
                         "single-volume closure, kept for A/B comparison")
    args = ap.parse_args()

    repos_root = Path(args.repos_root).resolve()
    policy_path = Path(args.policy).resolve() if args.policy else None
    universe, live, node_by_label, edges, issues, files = build(
        repos_root, args.repo_filter, args.root, policy_path, args.closure_scope
    )

    # notes-declared deps per owner (exclude proof files; handled separately)
    declared_notes: dict[str, dict[str, tuple[int, str]]] = {}
    block_line: dict[str, int] = {}
    for e in edges.edges:
        if Path(e.file).name.startswith("prf-"):
            continue
        declared_notes.setdefault(e.source, {})[e.target] = (e.line, e.display or "")
        block_line.setdefault(e.source, e.line)

    proofs = collect_proofs(files)
    text_cache: dict[str, str] = {}

    def file_text(rel: str) -> str:
        if rel not in text_cache:
            p = (repos_root / args.root / rel)
            if not p.exists():
                p = Path(rel)
            text_cache[rel] = p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
        return text_cache[rel]

    adds: list[tuple] = []
    removes: list[tuple] = []
    creates: dict[str, list] = {}
    proof_unused: list[tuple] = []

    audited_nodes = [n for n in universe.nodes if n.repo == args.root and n.kind in {"thm", "lem", "prop", "cor", "def"}]

    def name_tokens(label: str, display: str) -> list[str]:
        raw = re.split(r"[:\-\s]", label.split(":", 1)[-1]) + re.split(r"[\s]", display.lower())
        return [w for w in (t.strip().lower() for t in raw) if len(w) >= 5]

    for n in audited_nodes:
        L = n.label
        body = env_body(file_text(n.file), L) or ""
        stmt_refs = {t for t in (m.group(1).strip() for m in HREF.finditer(strip_dep_blocks(body)))
                     if is_formal(t) and t != L}
        decl = declared_notes.get(L, {})  # target -> (line, display)

        if n.kind == "def":
            prose = strip_dep_blocks(body).lower()
            used_explicit = set(stmt_refs)
            surface = "def"
        else:
            pf = proofs.get(L, {})
            prose = (strip_dep_blocks(body) + "\n" + pf.get("prose", "")).lower()
            used_explicit = set(stmt_refs) | set(pf.get("targets", set()))
            surface = "thm"

        used_by_prose = set()
        for t, (_ln, disp) in decl.items():
            toks = name_tokens(t, disp)
            if toks and any(w in prose for w in toks):
                used_by_prose.add(t)
        used = used_explicit | used_by_prose

        for t in (used_explicit | set(decl)):
            if t not in live:
                creates.setdefault(t, []).append((L, surface, n.file, decl.get(t, (n.line, ""))[0]))

        used_live = {t for t in used if t in live}
        decl_live = {t for t in decl if t in live}

        ins_line = block_line.get(L, n.line)
        for t in sorted({t for t in used_explicit if t in live} - decl_live):
            adds.append((surface, L, t, n.file, ins_line))
        for t in sorted(decl_live - used_live):
            removes.append((surface, L, t, n.file, decl[t][0]))

    for L, pf in proofs.items():
        if L not in node_by_label or node_by_label[L].repo != args.root:
            continue
        for t in pf["targets"]:
            if t not in live:
                creates.setdefault(t, []).append((L, "proof", pf["file"], pf["lines"].get(t, pf["block_line"])))
        prose = pf["prose"].lower()
        for t in pf["targets"]:
            if t not in live:
                continue
            toks = [w for w in re.split(r"[:-]", t.split(":", 1)[-1]) if len(w) > 3]
            if toks and not any(w in prose for w in toks):
                proof_unused.append((L, t, pf["file"], pf["lines"].get(t, pf["block_line"])))

    no_axiom = [(i.label, i.target, i.file, i.line) for i in issues
                if i.code == "closure_leaf_not_allowed_root"]

    # ---- markdown ----
    out = []
    out.append(f"# Dependency Correctness Audit — {args.root}")
    out.append(f"_Generated {_dt.datetime.now():%Y-%m-%d %H:%M} • {len(audited_nodes)} nodes audited • {len(proofs)} proofs • closure={args.closure_scope}_\n")
    out.append("## Summary\n")
    out.append(f"- **Add** dependency: {len(adds)}")
    out.append(f"- **Remove** dependency: {len(removes)}")
    out.append(f"- **Create** missing node: {len(creates)}")
    out.append(f"- **Proof dep not evident in prose** (verify): {len(proof_unused)}")
    out.append(f"- **Does not reach an axiom**: {len(no_axiom)}\n")

    out.append("## 1. Add dependency — actually used, not declared\n")
    out.append("_None._\n" if not adds else "")
    for surface, L, t, f, ln in sorted(adds):
        out.append(f"- **ADD** `{t}` to **{surface} `{L}`** — `{f}:{ln}`")
    out.append("")

    out.append("## 2. Remove dependency — declared, never used in statement or proof\n")
    out.append("_None._\n" if not removes else "")
    for surface, L, t, f, ln in sorted(removes):
        out.append(f"- **REMOVE** `{t}` from **{surface} `{L}`** — `{f}:{ln}`")
    out.append("")

    out.append("## 3. Create a missing node — referenced/declared but does not exist\n")
    if not creates:
        out.append("_None._\n")
    else:
        renames, writes = {}, {}
        for t in creates:
            hint = rename_hint(t, live)
            (renames if hint else writes)[t] = hint
        out.append(f"### 3a. Likely label fix — a live near-miss exists ({len(renames)})\n")
        for t in sorted(renames):
            who = ", ".join(sorted({lbl for lbl, _s, _f, _l in creates[t]})[:5])
            out.append(f"- **FIX** `{t}` → `{renames[t]}`  — used by: {who}")
        out.append(f"\n### 3b. Write-new — no live match; create the node ({len(writes)})\n")
        for t in sorted(writes):
            kind = t.split(":", 1)[0]
            who = ", ".join(sorted({lbl for lbl, _s, _f, _l in creates[t]})[:5])
            out.append(f"- **CREATE** `{t}`  _(a `{kind}`)_ — used by: {who}")
    out.append("")

    out.append("## 4. Proof dependency not evident in proof prose — verify or remove\n")
    out.append("_None._\n" if not proof_unused else "")
    for L, t, f, ln in sorted(proof_unused):
        out.append(f"- **VERIFY** proof of `{L}` declares `{t}` but prose may not use it — `{f}:{ln}`")
    out.append("")

    out.append(f"## 5. Does not reach an axiom (closure scope: {args.closure_scope})\n")
    out.append("_None._\n" if not no_axiom else "")
    for L, leaf, f, ln in sorted(no_axiom):
        tail = f" (chain stops at `{leaf}`)" if leaf else ""
        out.append(f"- `{L}`{tail} — `{f}:{ln}`")
    out.append("")

    outp = Path(args.out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text("\n".join(out), encoding="utf-8")
    print(f"audit[{args.closure_scope}]: {len(adds)} add, {len(removes)} remove, {len(creates)} create, "
          f"{len(proof_unused)} verify, {len(no_axiom)} no-axiom -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
