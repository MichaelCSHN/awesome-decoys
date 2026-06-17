# Awesome Decoys / 假目标与诱饵大全

[English](README.md) | 中文

这是一个围绕 **dummy / decoy / deception system** 的公开资料知识库。项目覆盖实体假目标、信号诱饵、网络诱饵、反诱饵鉴别、历史欺骗案例、现代冲突案例、产业图谱和自主式假飞机系统（ADAS）等方向。

## 快速入口

- 交互式案例浏览器：[assets/cases-explorer.html](assets/cases-explorer.html)，如已启用 GitHub Pages，也可访问 [michaelcshn.github.io/awesome-decoys/assets/cases-explorer.html](https://michaelcshn.github.io/awesome-decoys/assets/cases-explorer.html)
- 分类体系：[docs/taxonomy.zh-CN.md](docs/taxonomy.zh-CN.md)
- 案例库字段：[docs/case-schema.zh-CN.md](docs/case-schema.zh-CN.md)
- 来源表字段：[docs/source-schema.zh-CN.md](docs/source-schema.zh-CN.md)
- 网络诱饵专题：[docs/cyber-decoys.zh-CN.md](docs/cyber-decoys.zh-CN.md)
- 反诱饵与鉴别：[docs/counter-decoy.zh-CN.md](docs/counter-decoy.zh-CN.md)
- 自主式假飞机系统：[docs/adas.zh-CN.md](docs/adas.zh-CN.md)
- 厂商与市场图谱：[docs/vendors.zh-CN.md](docs/vendors.zh-CN.md)
- 数据文件说明：[data/README.zh-CN.md](data/README.zh-CN.md)
- 贡献指南：[CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)

## 项目范围

本项目把假目标/诱饵理解为一种通用方法：通过构造对象、信号、行为、身份、系统或叙事，让观察者、传感器、算法、武器、入侵者或决策者产生错误判断，进而错误分配注意力、弹药、时间、算力或行动。

核心维度包括：

- **时间维度**：古代诈术、工业化时代、两次世界大战、冷战与精确打击时代、当代透明战场、智能化未来。
- **特征维度**：实体、信号、行为、网络、叙事/情报。
- **物理演进维度**：经典式、机械化、信息化、智能化。
- **技术生命周期**：设计/生成、生产/制造、部署/运用、测试/评估。
- **领域维度**：陆、空、海、潜、天、电磁频谱、网络、信息认知和跨域。
- **效果机制**：吸引火力、消耗弹药、拖延决策、过载 ISR、掩护机动、干扰 BDA、暴露敌方传感器、收集攻击者技战术。

## 数据结构

- `data/cases.csv`：核心案例库。
- `data/sources.csv`：结构化来源索引。
- `data/vendors.csv`：厂商与组织图谱。
- `references/sources.md`：面向阅读的来源索引。
- `references/source-wishlist.zh-CN.md`：信源缺口和补强优先级。
- `assets/cases-explorer.html`：离线、静态、可筛选的案例浏览器。

当前数据规模由校验脚本自动统计。运行：

```bash
python scripts/validate.py
```

## 来源分级

- **A**：主要官方/机构来源、研究报告、厂商对自身产品存在与规格的说明。
- **B**：可信媒体、专业防务媒体、署名专家文章。
- **C**：二次聚合、博客、市场报告、单一来源分析。
- **D**：未核实社交媒体、图片/视频片段、需要独立地理定位和时间核实的材料。

来源类型和质量等级是两个独立维度。厂商页面可以是产品存在的 A 级来源，但不能自动证明作战效果。

## 当前重点专题

- 历史欺骗：坚忍行动、幽灵部队、Q 船、Starfish 诱饵场、肉馅行动。
- 现代冲突：纳卡 An-2 诱饵压制防空、俄乌 HIMARS/机场/充气假目标、以伊导弹饱和与突防辅助、红海低成本消耗。
- 信号诱饵：箔条、热焰弹、TALD/MALD、拖曳诱饵、Nulka、Nixie、弹道导弹突防辅助。
- 网络诱饵：蜜罐、蜜标、假凭证、假身份、欺骗网络、MITRE Engage/D3FEND。
- 反诱饵：多谱段一致性、SAR 散射、红外/运动学鉴别、BMD 中段鉴别、pattern-of-life、多源情报融合、AI/ATR 鲁棒性。
- ADAS：面向机场生存力和分布式航空作战的自主式假飞机系统。

## 维护原则

- 不把“厂商声称”当作“作战验证”。
- 对估算数字、拦截率、成本交换、战果评估保留来源和不确定性。
- 先补来源，再补案例。
- 每次修改后运行 `python scripts/validate.py`。

## 许可

本项目原创元数据、分类文本、schema 和说明采用 CC BY 4.0。外部链接、文章、图片、报告、商标和产品材料仍归原权利人所有。
