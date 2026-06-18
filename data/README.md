# Data Files

[English](README.md) | [中文](README.zh-CN.md)

This directory contains the structured backbone of the project.

## Files

- `cases.csv` - Case database. Each row is a historical case, modern conflict example, product/concept, cyber decoy, or counter-decoy method.
- `claims.csv` - Claim-level evidence table. Each row links a specific claim to one case and one or more sources, with claim type and confidence.
- `sources.csv` - Structured source index keyed by `source_key`.
- `vendors.csv` - Vendor and organization map keyed by `vendor_key`.

## Relationships

- `data/cases.csv` uses `source_refs` to point to `data/sources.csv`.
- `data/claims.csv` uses `case_id` to point to `data/cases.csv` and `source_refs` to point to `data/sources.csv`.
- `references/sources.md` is the human-readable source index.
- `assets/cases-explorer.html` embeds the current case dataset for offline browsing.

## Validation

Run from the repository root:

```bash
python scripts/build_explorer.py --check
python scripts/validate.py
```
