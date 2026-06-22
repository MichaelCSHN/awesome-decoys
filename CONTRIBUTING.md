# Contributing

Contributions should improve the encyclopedia without weakening source traceability.

## Add a Case

1. Add one row to `data/cases.csv`.
2. Use a stable `case_id` prefix:
   - `HIST-` for historical cases.
   - `MOD-` for modern conflict cases.
   - `IND-` for industry/product cases.
   - `CYBER-` for cyber deception.
   - `CD-` for counter-decoy/discrimination methods.
   - `CONCEPT-` for concepts or adjacent initiatives.
3. Keep `source_refs` as semicolon-separated source keys.
4. Make uncertainty explicit in `notes`.
5. Do not promote vendor or media claims into validated effects unless a stronger source supports it.

## Add a Source

1. Add the source to `references/sources.md` for human reading.
2. Add the same `source_key` to `data/sources.csv`.
3. Classify `source_type` and `quality_tier` using `docs/source-schema.md`.
4. Prefer direct primary URLs. Add caveats in `notes` for paywalls, single-outlet claims, redirects, or estimates.

## Add a Vendor

1. Add one row to `data/vendors.csv`.
2. Include a URL when possible.
3. Use `notes` to distinguish verified product pages from market-report mentions.

## Validate

Run:

```bash
python scripts/build_explorer.py --check
python scripts/validate.py
```

The script checks CSV parsing, duplicate keys, case-to-source references, local links, and whether
`assets/cases-explorer.html` is synchronized with `data/cases.csv`.
