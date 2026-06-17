# 贡献指南

本项目欢迎补充案例、来源、厂商和专题，但所有新增内容都应保持可追溯、可校验。

## 新增案例

1. 在 `data/cases.csv` 新增一行。
2. 使用稳定的 `case_id` 前缀：
   - `HIST-`：历史案例。
   - `MOD-`：现代冲突案例。
   - `IND-`：产业/产品案例。
   - `CYBER-`：网络诱饵案例。
   - `CD-`：反诱饵/鉴别方法。
   - `CONCEPT-`：概念、倡议或邻近能力。
3. `source_refs` 使用分号分隔来源键。
4. 在 `notes` 中明确不确定性、争议和来源限制。
5. 厂商或媒体声称不能直接等同于已验证作战效果，除非有更强来源支撑。

## 新增来源

1. 在 `references/sources.md` 中加入便于阅读的来源条目。
2. 在 `data/sources.csv` 中加入同一个 `source_key`。
3. 按 `docs/source-schema.md` 选择 `source_type` 和 `quality_tier`。
4. 优先使用直接、主要来源；对付费墙、单一来源、重定向和估算数据，在 `notes` 中说明。

## 新增厂商

1. 在 `data/vendors.csv` 新增一行。
2. 尽量提供官方网站。
3. 用 `notes` 区分“已核实产品页面”和“市场报告中提及”。

## 校验

运行：

```bash
python scripts/validate.py
```

脚本会检查 CSV 解析、重复键、案例与来源引用、本地链接，以及 `assets/cases-explorer.html`
是否与 `data/cases.csv` 同步。
