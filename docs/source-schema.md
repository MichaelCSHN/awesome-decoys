# Source Database Schema

[English](source-schema.md) | [中文](source-schema.zh-CN.md)

`data/sources.csv` is the structured source index. It complements the human-readable
[`references/sources.md`](../references/sources.md): the markdown file groups sources by topic
for reading, while the CSV makes the **source-type** and **quality-tier** dimensions queryable
and keeps source keys consistent with [`data/cases.csv`](../data/cases.csv).

## Fields

| Field | Meaning | Example |
|---|---|---|
| `source_key` | Stable key, identical to the keys used in `cases.csv` `source_refs` and in `references/sources.md` | `FPRI-SHALLOW-RAMPARTS` |
| `title` | Title of the work | `Shallow Ramparts: Air and Missile Defenses in the June 2025 Israel-Iran War` |
| `publisher` | Issuing body, outlet, or vendor | `Foreign Policy Research Institute` |
| `source_type` | Genre/provenance from the controlled vocabulary below | `think_tank_report` |
| `quality_tier` | A/B/C/D evidentiary tier (claim-dependent) | `A/B` |
| `url` | Direct link | `https://www.fpri.org/article/2025/10/...` |
| `notes` | Caveats, scope of reliability, stub status | `tier inferred per project rules` |

## `source_type` Controlled Vocabulary

`peer_reviewed_journal`, `conference_paper`, `book`, `think_tank_report`,
`gov_military_official`, `military_professional_journal`, `trade_defense_media`,
`news_media`, `vendor_industry`, `analysis_blog`, `reference_encyclopedic`, `software_repo`, `osint_social`,
`dataset_database`, `institutional_reference`, `standard_patent_spec`.

Definitions and Chinese glosses are maintained in [`docs/taxonomy.md`](taxonomy.md),
section 6, "Source Type / Provenance".

## Two Orthogonal Axes

`source_type` and `quality_tier` are independent:

- Source **type** answers "what kind of artifact is this?"
- Quality **tier** answers "how much weight does it carry, and for which claim?"

A single source can warrant different tiers for different claims. The canonical example:
a vendor product page is Tier A evidence that a product *exists and is marketed with stated
specs*, but Tier D evidence that it *defeats a given sensor in combat*. Record the claim-specific
caveat in `notes`, and keep product claims separate from validated battlefield effects.

## Quality-Tier Reference (same as `references/sources.md`)

- **A** - Primary official / institutional: doctrine, official military articles, government
  reports, RAND-class research, vendor pages for their own product existence and specs-as-claimed.
- **B** - Reputable reporting / specialist media: AP, RFE/RL, Forbes, The War Zone, professional
  defense media, named expert articles.
- **C** - Secondary aggregation: blogs, market reports, republications, unsourced summaries.
- **D** - Unverified / social: social media posts, videos, image-only claims pending
  independent geolocation, dating, and context checks.

## Normalization Rules

- Keep `source_key` stable and identical across `cases.csv`, `sources.csv`, and `sources.md`.
- Every `source_refs` key in `cases.csv` must resolve to a row here (run the integrity check below).
- Use one row per source. If a source supports several cases, reuse its key.
- Prefer the most authoritative `source_type` for the work itself, not for where it was reposted
  (e.g., a research-report chapter rehosted on an aggregator is still a report).
- Mark unfilled entries with a `notes` value beginning `STUB:`.

## Integrity Check

```python
import csv
keys = {r['source_key'] for r in csv.DictReader(open('data/sources.csv'))}
missing = set()
for row in csv.DictReader(open('data/cases.csv')):
    for k in row['source_refs'].split(';'):
        k = k.strip()
        if k and k not in keys:
            missing.add(k)
print(sorted(missing) or 'consistent')
```
