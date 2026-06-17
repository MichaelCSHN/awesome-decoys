# 案例库字段说明

[English](case-schema.md) | 中文

`data/cases.csv` 是项目的核心案例库。

## 当前字段

| 字段 | 含义 |
|---|---|
| `case_id` | 稳定案例 ID |
| `name_zh` | 中文名称 |
| `name_en` | 英文名称 |
| `period` | 年份、时代或冲突阶段 |
| `actor` | 国家、部队、组织、厂商或倡议 |
| `conflict_context` | 战争、战役、演习、市场或概念背景 |
| `target_or_platform` | 诱饵模仿或保护的对象 |
| `decoy_form` | 实体、信号、行为、网络、叙事、自主或混合形式 |
| `mobility` | 静态、可搬移、机动、遥控、自主 |
| `spectral_features` | EO、IR、SAR/雷达、RF、声学、网络、行为、多谱段 |
| `deception_effect` | 预期或观察到的欺骗效果 |
| `source_quality` | A/B/C/D 来源等级 |
| `source_refs` | 来源键，分号分隔 |
| `notes` | caveat、争议和研究备注 |
| `feature_dimension` | `physical`、`signal`、`behavioral`、`cyber`、`narrative`、`mixed` |
| `domain` | `land`、`air`、`sea`、`space`、`ems`、`cyber`、`information`、`cross_domain` |
| `physical_evolution` | `classic`、`mechanical`、`informationized`、`intelligent` |

## 新增案例规则

- 每个案例必须至少有一个可追溯来源。
- `source_refs` 中的每个键都必须存在于 `data/sources.csv`。
- 对估算数字、战果、拦截率、成本交换和单一来源报道，应在 `notes` 中说明。
- 产品页只证明产品存在和厂商声明，不证明战场效果。

## 未来可扩展字段

- `time_dimension`
- `target_class`
- `observer_victim`
- `effect_mechanism`
- `fidelity_level`
- `maturity_level`
- `cost_scalability`
- `counter_decoy_methods`
- `evidence_strength`
- `source_dates`
