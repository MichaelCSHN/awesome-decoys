# 数据文件说明

[English](README.md) | [中文](README.zh-CN.md)

本目录是项目的结构化数据核心。

## 文件

- `cases.csv` - 案例库。每一行可以是历史案例、现代冲突案例、产品/概念、网络诱饵或反诱饵方法。
- `sources.csv` - 结构化来源索引，以 `source_key` 为主键。
- `vendors.csv` - 厂商与组织图谱，以 `vendor_key` 为主键。

## 关系

- `data/cases.csv` 通过 `source_refs` 引用 `data/sources.csv`。
- `references/sources.md` 是面向阅读的来源索引。
- `assets/cases-explorer.html` 内嵌当前案例库，用于离线浏览和筛选。

## 校验

在仓库根目录运行：

```bash
python scripts/validate.py
```
