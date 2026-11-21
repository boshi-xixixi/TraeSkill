---
name: trae-project-setup
description: Trae 项目规范化配置专家。用于快速初始化 Trae 项目配置文件、生成项目规则、用户偏好设置和 Skill 模板。当用户需要：(1) 初始化新项目的 Trae 配置 (2) 生成 .trae 目录结构 (3) 创建 USER_PREFERENCES.md 用户偏好文件 (4) 创建 project_rules.md 项目规则文件 (5) 创建新的 Skill 模板 时使用此 Skill。 触发词：初始化项目、生成 .trae、项目规范配置、新建项目脚手架。
---
# Trae Project Setup

本 Skill 用于快速生成 Trae 项目所需的规范化配置文件，帮助项目实现标准化开发流程。

## Trae 配置体系概述

Trae 通过 `.trae` 目录管理项目配置，支持以下核心文件：

| 文件路径 | 用途 | 优先级 |
|---------|------|--------|
| `.trae/USER_PREFERENCES.md` | 用户偏好设置（语言、技术栈、交互风格） | 最高 |
| `.trae/rules/project_rules.md` | 项目特定规则（lint、typecheck、构建命令） | 高 |
| `.trae/Skills/` | 自定义 Skill 目录 | 中 |

## 快速开始

### 初始化项目配置

运行初始化脚本，自动创建完整的 `.trae` 目录结构：

```bash
python scripts/init_trae_project.py --path /path/to/project
```

脚本会自动创建：
- `.trae/USER_PREFERENCES.md` - 用户偏好模板
- `.trae/rules/project_rules.md` - 项目规则模板
- `.trae/Skills/` - Skill 存放目录

### 验证项目配置

验证现有配置是否符合规范：

```bash
python scripts/validate_trae_project.py --path /path/to/project
```

## 核心配置文件详解

### USER_PREFERENCES.md

用户偏好文件，定义全局行为模式。Trae 会在所有操作中优先遵循此文件的设置。

**关键配置项：**

```markdown
# User Preferences

## 1. 技术栈偏好 (Tech Stack)
*   **CSS Framework**: Tailwind CSS
*   **State Management**: Zustand (React), Riverpod (Flutter)
*   **Testing**: Vitest
*   **Language**: TypeScript (Strict Mode)

## 2. 交互风格 (Communication Style)
*   **Language**: 中文回复，技术术语保留英文
*   **Detail Level**: 资深开发者模式，直接给代码
*   **Emoji**: 禁用

## 3. 角色覆盖 (Role Overrides)
*   **@Backend Developer**: 优先使用 FastAPI

## 4. 禁令 (Constraints)
*   严禁使用 `any` 类型
*   严禁创建 `.env` 文件
```

### project_rules.md

项目规则文件，定义项目特定的开发规范。

**关键配置项：**

```markdown
# Project Rules

## 构建与验证命令
*   **Lint**: npm run lint
*   **TypeCheck**: npm run typecheck
*   **Test**: npm run test
*   **Build**: npm run build

## 代码规范
*   **函数注释**: 必须添加函数级注释
*   **语言**: 中文注释，外链库需在中国可用

## Git 规范
*   **Commit**: 遵循 Conventional Commits
*   **Branch**: feature/*, fix/*, docs/*
```

## 创建新 Skill

### 使用初始化脚本

```bash
python scripts/init_trae_skill.py <skill-name> --path .trae/Skills
```

### Skill 目录结构

```
skill-name/
├── SKILL.md          # 必需：Skill 主文件
├── scripts/          # 可选：可执行脚本
├── references/       # 可选：参考文档
├── assets/           # 可选：资源文件
└── AGENTS.md         # 可选：Agent 定义
```

### SKILL.md 格式

```markdown
---
name: skill-name
description: Skill 描述，包含触发条件和使用场景
---

# Skill Title

## Overview
简要说明 Skill 功能

## Workflow
1. 步骤一
2. 步骤二
```

### AGENTS.md 格式

```markdown
---
name: agent-name
description: Agent 描述
---

# Agent Title

## 角色定义
*   **专长**: 描述专业领域
*   **风格**: 描述工作风格

## 工作流程
1. 步骤一
2. 步骤二
```

## 模板文件

完整的模板文件存放在 `templates/` 目录：

- `USER_PREFERENCES.md.template` - 用户偏好模板
- `project_rules.md.template` - 项目规则模板
- `SKILL.md.template` - Skill 模板
- `AGENTS.md.template` - Agent 模板

## 参考文档

详细规范请参阅：
- [Trae 配置规范](references/trae_configuration_spec.md)
- [Skill 开发指南](references/skill_development_guide.md)
