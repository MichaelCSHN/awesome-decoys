# Claim 级证据表字段说明

[English](claim-schema.md) | 中文

`data/claims.csv` 记录 claim 级证据。它补充 `data/cases.csv`：案例是一组事件、系统、方法或概念；claim 是案例中的一个具体说法，可以单独引用来源并赋予置信度。

当一个案例包含多个不应混用证据权重的说法时，应使用 claims，例如产品存在、部署报道、诱饵效果、成本交换、技术机制、争议性战果或 BDA。

## 字段

| 字段 | 含义 |
|---|---|
| `claim_id` | 稳定 claim 标识。 |
| `case_id` | 来自 `data/cases.csv` 的既有案例 key。 |
| `claim_type` | 受控词表：`existence`、`deployment`、`effect`、`mechanism`、`cost_exchange`、`technical`、`context`、`uncertainty`。 |
| `claim` | 被断言的简短说法。 |
| `confidence` | 受控词表：`confirmed`、`corroborated`、`reported`、`provisional`、`contested`。 |
| `source_refs` | 以分号分隔的 `data/sources.csv` 来源 key。 |
| `notes` | caveat、适用范围或来源质量提醒。 |

## 置信度规则

- `confirmed` - 官方、机构、档案、技术或一手来源直接支持该说法。
- `corroborated` - 多个可信来源支持该说法，但不一定全是一手来源。
- `reported` - 可信报道提出该说法，但独立验证有限。
- `provisional` - 说法合理且相关，但依赖有限或间接证据。
- `contested` - 来源互相冲突，或该说法存在实质争议。

## 规范化规则

- claim 应简短、可检验。
- 不要把产品存在、部署和战场效果混在同一个 claim。
- 不要只用厂商来源证明作战效果。
- 对重要但弱来源支撑的内容，用 `uncertainty` claim 保留，而不是过度断言。
- 修改后运行 `python scripts/validate.py`。
