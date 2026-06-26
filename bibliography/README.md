# Volume Bibliography

This directory is owned by `lra-volume-ii`.

Bibliography shards are book-owned and used directly by this volume repository. They are not copied to a monorepo or to `lra-common`.

Current shards:

- `volume-ii-discrete-number-systems.bib`
- `volume-ii-the-continuum.bib`

Add entries only to the shard for the owning book root, then run:

```powershell
python scripts/check_bibliography.py --bib-dir bibliography
```

Do not add unrelated volume bibliography files here.
