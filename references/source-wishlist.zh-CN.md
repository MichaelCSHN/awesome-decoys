# 信源补强清单

[English](source-wishlist.md) | 中文

本文件用于跟踪信源缺口。它和 [`sources.md`](sources.md) 分工不同：`sources.md`
记录已经纳入项目的来源，本文件记录下一步应该补强什么。

## 覆盖目标

一个案例要算作证据较稳，应尽量满足：

- 至少有两个相互独立的 `source_refs`。
- 至少一个来源为 A 或 A/B 级。
- 现代冲突中的战果、毁伤、消耗、拦截率等效果类说法，应由不止一个来源交叉印证；否则必须标注为 reported / provisional。
- 厂商页面只用于证明产品存在和厂商自称规格，不能直接证明实战效果。
- 技术方法优先使用同行评审论文、专利/规范、官方测试报告、军方研究报告；博客解释只作辅助。

## 优先补强队列

| 优先级 | 领域 | 当前弱点 | 目标来源 |
|---|---|---|---|
| P0 | 近期单一来源说法 | `CONCEPT-2026-LUCAS-EPICFURY` 仍依赖一篇近期文章 | 寻找官方声明、演训/行动记录、采购痕迹，或至少两个独立国防媒体确认 |
| P0 | 俄乌战场假目标效果 | 打击次数、诱骗成功、BDA 多数仍是媒体报道 | 只纳入已归档且可交叉校验的地理定位 OSINT；优先官方说法加独立影像分析 |
| P1 | 二战 Starfish 诱饵场 | `HIST-WWII-STARFISH` 仍偏依赖二手可视化文章 | 补 UK National Archives、Historic England、IWM 或官方民防史 |
| P1 | 胡塞红海诱饵与发射车生存 | 地面诱饵和机动发射车说法较间接 | 补 CENTCOM、UKMTO、US Navy、CRS/GAO、IISS、RUSI 或 CSIS Missile Defense |
| P1 | 红外/多谱段反诱饵鉴别 | 部分方法案例仍使用概括性解释来源 | 补 SPIE/IEEE/DTIC/NATO STO 关于成像红外鉴别、多谱段目标识别、SAR/EO 融合的论文 |
| P1 | 太空诱饵与反诱饵鉴别 | 现有太空覆盖主要集中在弹道导弹中段突防诱饵 | 补 MDA、GAO、CRS、CSIS、RAND、IAC/AIAA、天体动力学论文中的中段鉴别、卫星诱饵/抵近操作、空间态势感知、充气/反射体目标来源 |
| P1 | 水下诱饵与无人水下系统 | 已有 Nixie，但水下软杀伤、声学对抗、UUV 假目标覆盖偏薄 | 补鱼雷防御手册、NATO STO/ONR 论文、厂商规格、机动声学诱饵、可消耗声学装置、UUV 假目标研究 |
| P1 | AI / ATR / 自主反诱饵 | 已有 ATR 与对抗鲁棒性，但 AI 生成诱饵和自主欺骗规划不足 | 补 SAR/EO ATR、物理对抗样本、生成式伪装、仿真到现实目标合成、自主多智能体欺骗研究 |
| P1 | 无人/自主诱饵系统 | An-2 与 LUCAS 类案例需要更宽背景 | 补巡飞诱饵、MALD-X/MALD-N、无人机搭载 RF 发射器、可消耗僚机诱饵角色、自主蜂群诱饵、演训/测试来源 |
| P2 | 网络反蜜罐 | `CYBER-ANTI-HONEYPOT` 仍主要来自工具清单和解释文章 | 补蜜罐指纹识别、攻击者交互、欺骗系统评估方面的学术研究 |
| P2 | 厂商目录 | 产品列表已有，但不少缺少归档、代际和谱段归一化 | 补 PDF、归档页面、专利族、采购公告，按主要厂商/产品族整理 |

## 搜索建议

优先使用定向检索：

- `site:dtic.mil decoy deception infrared flare imaging seeker discrimination`
- `site:apps.dtic.mil multispectral target recognition decoy discrimination`
- `site:spiedigitallibrary.org infrared countermeasure flare discrimination`
- `site:ieeexplore.ieee.org SAR decoy discrimination polarimetric`
- `site:gao.gov decoy deception missile defense discrimination`
- `site:crsreports.congress.gov deception decoy missile defense`
- `site:mda.mil discrimination decoys countermeasures missile defense`
- `site:csis.org missile defense decoys discrimination space`
- `site:rand.org space deception decoy counterspace`
- `site:navalpostgraduate.edu torpedo decoy acoustic countermeasure`
- `site:onr.navy.mil acoustic decoy unmanned undersea`
- `site:sto.nato.int decoy acoustic torpedo countermeasure`
- `site:darpa.mil MALD-X decoy autonomous electronic warfare`
- `site:afresearchlab.com autonomous decoy aircraft electronic warfare`
- `site:ieeexplore.ieee.org adversarial examples SAR ATR physical`
- `site:arxiv.org generative camouflage decoy target recognition`
- `site:discovery.nationalarchives.gov.uk Operation Mincemeat decoy`
- `site:nationalarchives.gov.uk Starfish decoy sites`
- `site:centcom.mil Houthi decoy launcher`

## 何时提升来源等级

只有证据姿态真实变强时，才提升案例质量：

- C 到 B：具名记者、专业媒体或专家文章提供了独立细节。
- B 到 A/B：军事专业期刊、具名从业者文章或技术论文支持了机制判断。
- A/B 到 A：官方/机构文档、档案记录、RAND 类报告、同行评审研究，或厂商对自身产品存在与自称规格的材料。

不要因为多个文章重复同一个上游说法，就提升质量等级。
