<!--
GENERATED FILE — DO NOT EDIT BY HAND.

Source repo: wsollers/lra-governance
Source commit: 0fe121116f1f6aa98359774a72c5fac67236e6a5
Generated from:
- docs/governance/...
- docs/architecture/...
- docs/governance/repo-overlays/lra-volume-ii.md

Regenerate from lra-governance.
Emergency downstream edits must be ported upstream before regeneration.
-->

# Copilot Instructions

Keep this file concise. Point to canonical docs and generated repo instructions
rather than embedding large governance manuals.

## Global Agent Rules

- Treat generated instruction files as derived artifacts.
- Follow the owning repository boundary for every task.
- Do not include secrets, credentials, tokens, or machine-local private values.
- Do not modify mathematical content during governance or wrapper-generation tasks.
- Do not touch the retired `Learning-Real-Analysis` monorepo.
- Keep context small: use governance docs as targeted references, not preload material.
- Open only the workflow, standard, schema, or overlay needed for the current task.
- Port emergency downstream instruction repairs back to `lra-governance`.

## Repo Overlay

# lra-volume-ii Overlay

Volume II uses the generic `lra-volume.md` overlay plus the additional
verification-link boundary below.

Owned concerns:

- Volume II content and Overleaf-ready source layout,
- stable theorem, definition, axiom, lemma, proposition, and corollary labels,
- cross-repository verification metadata that points to `lra-lean`,
- independent volume PDF builds published to `lra-volumes-output`.

## Agent Scope

Follow the generic volume overlay. Do not place formal proof implementation
work in `lra-volume-ii`; formal proof implementation is owned by `lra-lean`.

## Verification Links

Every theorem-like or definition-like artifact in Volume II should have a
stable LaTeX label that can be mapped to a formal verification target. When the
target is not available yet, record the status as pending rather than omitting
the relationship.

Volume II may carry lightweight verification metadata: LaTeX label,
verification status, target formalization repository, and target module or
declaration name when known.

Do not inline formal proof code as ordinary volume prose. The volume may point
to the formalization, but `lra-lean` owns checked formal source and any
implementation workflow. `lra-knowledge-explorer` owns the UI surface that
displays mapped verification code.

Use status wording that does not overclaim:

- `pending` when no target has been written,
- `statement` when a formal statement exists but the proof is incomplete,
- `checked` only when the target declaration is accepted by the formal build
  without placeholders for that declaration.

## Provider Notes

Keep provider-specific guidance concise and defer durable policy to governance docs.
