# 来源表字段说明

[English](source-schema.md) | 中文

`data/sources.csv` 是结构化来源索引，配合 `references/sources.md` 使用。

## 字段

| 字段 | 含义 |
|---|---|
| `source_key` | 稳定来源键，供 `data/cases.csv` 引用 |
| `title` | 来源标题 |
| `publisher` | 发布机构、媒体、厂商或仓库 |
| `source_type` | 来源类型 |
| `quality_tier` | 证据等级 |
| `url` | 直接链接 |
| `notes` | caveat、可靠性范围、占位说明 |

## 来源类型

常用值包括：

- `peer_reviewed_journal`
- `conference_paper`
- `book`
- `think_tank_report`
- `gov_military_official`
- `military_professional_journal`
- `trade_defense_media`
- `news_media`
- `vendor_industry`
- `analysis_blog`
- `reference_encyclopedic`
- `software_repo`
- `osint_social`
- `dataset_database`
- `institutional_reference`
- `standard_patent_spec`

## 质量等级

- **A**：官方、机构、研究报告、主要文献，或厂商对自身产品存在与规格的声明。
- **B**：可信媒体、专业媒体、署名专家文章。
- **C**：二次聚合、博客、市场报告、弱来源分析。
- **D**：未核实社交媒体、图片/视频、需要独立核实的材料。

来源类型和质量等级是两个独立维度。例如，厂商页面可以是产品存在的 A 级证据，但不能证明实战效果。
