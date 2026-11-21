# 更新日志

本文件记录 TraeSkill 的版本变更。格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

**怎么用**：如果你是 fork 或本地拷贝的使用者，看「同步建议」一列就知道这次要不要跟进。

| 变更类型 | 版本位 | 你要做什么 |
|---|---|---|
| 新增技能、增强现有技能能力 | MINOR | 想用新能力就同步 |
| 修正错误、修正链接、改措辞 | PATCH | 建议同步，成本低 |
| 删除技能、改变触发范围、调整目录结构 | MAJOR | 必须看说明再同步 |

## [未发布]

暂无。

## [1.3.0] - 2026-11-21

吸收外部开源方法论，增强 4 个技能的内容深度。**同步建议：建议同步**（内容增强，不改变调用方式）。

### 增强

- `03_Data_Analysis` 1.1.0：新增「对账与校验」8 条（Twyman 定律、合计行校验和、独立代码路径重算、份额池点名、派生列验证），新增「闸门能验什么 / 验不了什么」对照表
- `06_Writing_Technical` 1.1.0：新增报告原型选择（6 种）与五条硬规矩；去 AI 腔升级为四层模型，补充「减法天花板」与经验注入方法
- `02_Designer_WebGuidelines` 1.1.0：新增性能优化「先量再改」7 步，含可用性定义、护栏与棘轮、确定性代理指标、配对测量
- `02_Designer_FrontendImplementation` 1.1.0：新增界面八条范式、反向清单、「借一层不借一身」、「该是图的地方放真图」

### 说明

方法论来源为 huashu-excel、huashu-report、huashu-flash、tramstop-skill、huashu-design（均为 MIT 协议），已在各技能末尾标注出处。内容为提炼重写，非原文搬运。

## [1.2.0] - 2026-11-21

技能扩容与触发优化。**同步建议：想用新技能就同步**（新增目录，不影响已有技能）。

### 新增

- `01_PM_Research`：竞品分析、用户调研、RICE/KANO 优先级、指标体系与埋点
- `03_Data_Analysis`：数据清洗、EDA、图表选型、统计陷阱
- `05_DevOps_Deploy`：单机部署、Nginx、HTTPS、Docker Compose、线上排错
- `06_Writing_Technical`：论文与报告结构、引用规范、去 AI 腔
- `06_Writing_Presentation`：答辩与路演结构、时间控制、讲稿与问答

### 优化

- 39 个技能的 `description` 追加真实用户口语触发词，提升命中率
- `00_Meta_Dispatcher` 收紧触发范围，避免抢占单一领域任务的触发
- 补齐 28 个 `metadata.json` 与 13 个 `AGENTS.md`，45 个技能三件套齐备

### 修复

- 修正 README 与两份指南中缺失的目录条目，徽章数量更新为 45

## [1.1.0] - 2026-11-21

仓库瘦身与文档修复。**同步建议：已装过旧版的需要重新同步**（目录结构调整，旧路径会失效）。

### 变更

- 移除 342 个与仓库定位无关的第三方技能，体积从 16 MB 降至 3.8 MB
- 三个图表技能从 `.agents/skills/` 迁移到独立编号目录 `10_Diagram_*`，指南合并为 `10_Diagram_GUIDE.md`
- 删除未被任何文档引用的 `fireworks-tech-graph-main` 示例图残留

### 修复

- 全仓库 `.trae/skills` 大小写错误修正为 `.trae/Skills`（20 余处死链）
- 使用指南中指向不存在的 `universal-dev-team` 修正为 `00_Meta_UniversalDevTeam`
- 删除 README 中重复的 Cursor 支持章节
- 移除图表指南中的本机绝对路径
- `06_SEO_Technical` 的 Core Web Vitals 指标更新（FID 已退役，改用 INP）
- `scripts/validate_skills.py` 允许的编号范围补充 `10`

## [1.0.0] - 2026-01-22

首个版本。

### 新增

- 36 个角色化技能，覆盖产品、架构、设计、开发、测试、运维、办公、SEO、安全、AI、运营、元技能
- Cursor IDE 适配层 `cursor_adapter/`
- 技能依赖图谱 `SKILL_DEPENDENCIES.md`
- GitHub Actions 校验工作流
