# lra-volume-ii

**Volume II: Origins of Numbers** — Overleaf-ready standalone repository.

## Structure

```text
volume-ii.tex          — full-volume root (Overleaf main document)
volume-ii-<book>.tex   — individual book roots
common/               — shared LaTeX infrastructure supplied by lra-common; ignored here
bibliography/         — per-book bibliography shards
volume-ii/             — all LaTeX content for this volume
```

## Overleaf

Upload or checkout `common/` beside this repository's TeX roots, then set the main document to `volume-ii.tex` for the full volume or to one of the book roots:

```text
volume-ii-discrete-number-systems.tex, volume-ii-the-continuum.tex
```

`common/` is ignored by git in this volume repo; edit shared infrastructure in `lra-common`.

## Building locally

```powershell
python F:\repos\lra-governance\tools\governance\build_volume_docker.py --root F:\repos\lra-volume-ii --common-root F:\repos\lra-common
```
