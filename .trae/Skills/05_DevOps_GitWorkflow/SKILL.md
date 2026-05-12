---
name: git-workflow
description: 当用户需要规范化 Git 使用、进行代码协作或管理 Pull Request/Merge Request 时使用。此 Skill 提供 GitHub/Gitee 平台操作、Conventional Commits 规范及 PR/MR 最佳实践指导。
---

# Git Workflow & Platform Collaboration

本 Skill 旨在指导开发者规范化使用 Git，并高效利用 GitHub、Gitee 等代码托管平台进行协作。

## 包含的技能模块

### 1. 提交规范 (Commit Convention)
- **标准**: 遵循 [Conventional Commits](https://www.conventionalcommits.org/)。
- **格式**: `<type>(<scope>): <description>`
  - `feat`: 新功能
  - `fix`: 修补 bug
  - `docs`: 文档修改
  - `style`: 代码格式修改 (不影响代码运行的变动)
  - `refactor`: 重构 (即不是新增功能，也不是修改 bug 的代码变动)
  - `perf`: 性能优化
  - `test`: 增加测试
  - `chore`: 构建过程或辅助工具的变动
- **示例**: `feat(auth): add google oauth2 login support`

### 2. 分支策略 (Branching Strategy)
- **Trunk Based Development (推荐)**:
  - `main`: 随时可发布的主分支。
  - Feature branches: 短生命周期的功能分支，合并后即删除。
- **Git Flow (传统)**:
  - `master`, `develop`, `feature/*`, `release/*`, `hotfix/*`.

### 3. 平台特定指南 (Platform Specifics)

#### GitHub
- **Actions**: CI/CD 首选。
- **Pages**: 静态网站托管。
- **PR**: Pull Request 流程与 Code Review。

#### Gitee (码云)
- **国内加速**: 适合国内镜像与私有项目。
- **Gitee Go**: 内置的 CI/CD 流水线。
- **Pages**: Gitee Pages 服务。

## 🤖 智能体与 MCP 增强

### 推荐智能体角色
*   **Git Workflow Specialist**: 详见 [AGENTS.md](AGENTS.md)。
    *   专注于代码审查、提交信息规范化和发布流程管理。

### 推荐 MCP 工具
*   **Git MCP**:
    *   自动执行 `git add`, `git commit`, `git push`。
    *   分析 git log 生成 Changelog。
*   **GitHub MCP**:
    *   创建 Issue, 提交 PR, Review 代码, 管理 Releases。
*   **mcp-feedback-enhanced**:
    *   在生成 PR 描述或 Commit Message 时，如果上下文不足，使用 `ask_followup_question` 询问用户具体的修改原因或关联的 Issue。
    *   在进行 Code Review 时，使用该工具确认用户的 Review 重点。

---
