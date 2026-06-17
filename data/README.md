# Data Files

[English](README.md) | [中文](README.zh-CN.md)

This directory contains the structured backbone of the project.

## Files

- `cases.csv` - Case database. Each row is a historical case, modern conflict example, product/concept, cyber decoy, or counter-decoy method.
- `sources.csv` - Structured source index keyed by `source_key`.
- `vendors.csv` - Vendor and organization map keyed by `vendor_key`.

## Relationships

- `data/cases.csv` uses `source_refs` to point to `data/sources.csv`.
- `references/sources.md` is the human-readable source index.
- `assets/cases-explorer.html` embeds the current case dataset for offline browsing.

## Validation

Run from the repository root:

```bash
python scripts/validate.py
```
