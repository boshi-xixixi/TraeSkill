---
name: Backend Database Expert
description: 当用户需要进行数据库设计、SQL 优化或数据库迁移时使用。此 Skill 专注于提供数据库架构设计、性能调优和数据迁移策略的专业指导。
---

# Backend Database Skills

## 🤖 智能体与 MCP 增强 (Agent & MCP Enhancements)

本 Skill 支持并推荐配合特定的智能体角色和 MCP 工具使用，以获得最佳效果。

### 推荐智能体角色
*   **Database Consultant**: 详见 [AGENTS.md](AGENTS.md)。
    *   该角色专注于数据库架构设计、性能调优和数据安全。
    *   启用后，AI 将优先进行 Schema 内省和执行计划分析。

### 推荐 MCP 工具
*   **PostgreSQL/MySQL MCP**: 允许 AI 直接连接数据库，获取实时的 Schema 信息和执行 EXPLAIN 分析，而不仅仅是基于静态代码推断。
*   **mcp-feedback-enhanced**: 允许 AI 在设计表结构或优化策略时，如果遇到不确定性，使用 `ask_followup_question` 等工具主动向用户确认业务需求或权衡方案。

---

提供专业的数据库开发与维护能力，帮助你构建高性能、高可靠的数据层。

## 包含的技能模块

### 1. [SQL 优化模式 (SQL Optimization)](./SQL优化模式.md)
- **核心价值**: 解决慢查询，提升数据库性能。
- **关键技术**: EXPLAIN 分析, 索引策略, N+1 问题修复.
- **使用场景**: 数据库性能瓶颈分析、复杂查询优化。

### 2. [数据库迁移 (Database Migration)](./数据库迁移.md)
- **核心价值**: 安全、可控地变更数据库结构。
- **关键技术**: 迁移脚本编写, 向后兼容性, 零停机迁移.
- **使用场景**: 版本迭代、Schema 变更、数据清洗。

## 如何使用

- **性能调优**: "请使用 SQL 优化模式帮我分析这条查询语句为什么这么慢。"
- **结构变更**: "请参考数据库迁移指南，帮我写一个给用户表添加字段的迁移脚本。"
