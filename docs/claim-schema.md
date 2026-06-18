# Claim Evidence Schema

[English](claim-schema.md) | [中文](claim-schema.zh-CN.md)

`data/claims.csv` records claim-level evidence. It complements `data/cases.csv`: a case is a grouped event, system, method, or concept; a claim is one specific statement inside that case that can be sourced and assigned a confidence level.

Use claims when a case contains separable statements that should not share the same evidence weight, such as product existence, deployment, effect, cost-exchange, technical mechanism, and uncertain battle-damage claims.

## Fields

| Field | Meaning |
|---|---|
| `claim_id` | Stable claim identifier. |
| `case_id` | Existing key from `data/cases.csv`. |
| `claim_type` | Controlled vocabulary: `existence`, `deployment`, `effect`, `mechanism`, `cost_exchange`, `technical`, `context`, `uncertainty`. |
| `claim` | Short statement being asserted. |
| `confidence` | Controlled vocabulary: `confirmed`, `corroborated`, `reported`, `provisional`, `contested`. |
| `source_refs` | Semicolon-separated source keys from `data/sources.csv`. |
| `notes` | Caveats, scope limits, or source-quality warning. |

## Confidence Rules

- `confirmed` - Direct official, institutional, archival, technical, or primary evidence supports the claim.
- `corroborated` - Multiple credible sources support the claim, but not all are primary.
- `reported` - A credible report states the claim, but full independent verification is limited.
- `provisional` - Plausible and relevant, but dependent on limited or indirect evidence.
- `contested` - Sources disagree or the claim is materially disputed.

## Normalization Rules

- Keep claims short and testable.
- Do not mix product existence, deployment, and battlefield effect in the same claim.
- Do not use a vendor source alone to prove operational effectiveness.
- Use `uncertainty` claims to preserve important but weakly sourced points without overstating them.
- Run `python scripts/validate.py` after editing.
