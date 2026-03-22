# Trae Skills 使用指南 (Trae Skills Guide)

欢迎使用 Trae Skills 技能库！这是一套经过精心编排的、角色导向的开发能力集。

我们按照**软件开发生命周期 (SDLC)** 和 **专业角色** 对技能进行了分类，每个技能目录都包含一个 `SKILL.md`，Trae 可以直接读取并扮演相应的专家角色。

## 🚀 如何使用

在与 Trae 对话时，你可以直接呼叫特定的角色或技能编号：

> "作为 **01 号产品经理**，请帮我..."
> "请使用 **03 号 Flutter 专家** 的技能帮我..."
> "启动 **05 号数据库专家** 帮我优化 SQL..."

**💡 进阶：[查看开发技能场景指南](./开发常用技能及场景指南.md)**

---

## 🤖 智能体与 MCP 配置指南 (Agent & MCP Configuration)

在 Trae 中使用这些 Skills，有两种推荐的配置模式。

### 模式一：自动读取 (Auto-Read Context) - *开箱即用*
Trae 会自动索引 `.trae/skills` 下的所有 Markdown 文件。
*   **适用场景**: 快速查询规范、获取通用建议、轻量级任务。
*   **如何使用**: 直接在对话中说“参考 React 最佳实践”或“作为产品经理帮我分析”。
*   **局限性**: 无法直接绑定 MCP 工具，主要依靠 AI 生成代码或命令。

### 模式二：手动配置 (Manual Agent Config) - *专家模式*
为了获得**最佳体验**（特别是涉及 MCP 工具调用时），建议在 Trae 的设置中手动创建对应的 Agent智能体。

*   **配置步骤**:
    1.  打开 Trae 在智能体页面选择“创建智能体”。
    2.  **新建智能体**:
        *   **自动构建提示词**: 复制对应 Skill 下的 `AGENTS.md` 内容 (如 `.trae/skills/06_Office_Docx/AGENTS.md`)。
        *   **配置MCP**: 在配置界面勾选该角色需要的 MCP Server (如 `filesystem`, `postgresql` 等)。
    3.  **保存**。

*   **使用方法**: 在对话框输入 `@<智能体名称>` 即可激活该“完全体”智能体。
*   **优势**: 
    *   **工具绑定**: 只有手动配置的 Agent 才能稳定地拥有特定的 MCP 工具权限。
    *   **角色纯度**: System Prompt 的权重更高，AI 不容易“出戏”。

**💡 建议**: 对于常用的重型工具类 Skill (如 Database, Office, Security)，强烈建议采用**模式二**进行配置。

---

## 📚 技能目录 (Skill Catalog)

### 💡 01. Product Manager (产品经理)
**目标**: 将模糊的想法转化为清晰的需求。
- **[01_ProductManager_Brainstorming](.trae/skills/01_ProductManager_Brainstorming/SKILL.md)**: 深度头脑风暴与需求挖掘。

### 📐 02. Architect & Designer (架构与设计)
**目标**: 确立技术方案与视觉规范.
- **[02_Architect_APIDesign](.trae/skills/02_Architect_APIDesign/SKILL.md)**: REST/GraphQL API 设计专家。
- **[02_Designer_WebGuidelines](.trae/skills/02_Designer_WebGuidelines/SKILL.md)**: Vercel 级 Web 设计规范。
- **[02_Designer_FrontendImplementation](.trae/skills/02_Designer_FrontendImplementation/SKILL.md)**: 前端落地设计指南。

### 💻 03. Client Developer (客户端开发)
**目标**: 构建高质量的用户界面。
- **[03_Developer_ReactBestPractices](.trae/skills/03_Developer_ReactBestPractices/SKILL.md)**: React/Next.js 性能与规范专家。
- **[03_Developer_ArtifactsBuilder](.trae/skills/03_Developer_ArtifactsBuilder/SKILL.md)**: 现代 UI 组件构建器。
- **[03_Mobile_Flutter](.trae/skills/03_Mobile_Flutter/SKILL.md)**: Flutter 整洁架构与性能优化专家。

### 🧪 04. Tester / QA (测试与自动化)
**目标**: 确保软件质量与自动化执行。
- **[04_Tester_BrowserAutomation](.trae/skills/04_Tester_BrowserAutomation/SKILL.md)**: 浏览器自动化操作与测试。

### ⚙️ 05. Backend & DevOps (后端与运维)
**目标**: 构建稳固的后端服务与部署流程。
- **[05_Backend_Python](.trae/skills/05_Backend_Python/SKILL.md)**: FastAPI、异步编程与性能优化。
- **[05_Backend_Node](.trae/skills/05_Backend_Node/SKILL.md)**: Node.js 架构模式。
- **[05_Backend_Database](.trae/skills/05_Backend_Database/SKILL.md)**: SQL 优化与数据库迁移。
- **[05_Backend_MCPBuilder](.trae/skills/05_Backend_MCPBuilder/SKILL.md)**: MCP Server 构建专家。
- **[05_DevOps_GitOps](.trae/skills/05_DevOps_GitOps/SKILL.md)**: Kubernetes GitOps 部署流。
- **[05_DevOps_GitWorkflow](.trae/skills/05_DevOps_GitWorkflow/SKILL.md)**: Git 提交规范、GitHub/Gitee 平台协作指南。

### 📂 06. Office Utilities (办公助手)
**目标**: 处理复杂的办公文档。
- **[06_Office_Docx](.trae/skills/06_Office_Docx/SKILL.md)**: Word 文档处理。
- **[06_Office_Excel](.trae/skills/06_Office_Excel/SKILL.md)**: Excel 数据分析。
- **[06_Office_Pdf](.trae/skills/06_Office_Pdf/SKILL.md)**: PDF 处理与提取。

### 🛡️ 07. Security Specialist (安全专家)
**目标**: 保障应用与数据安全。
- **[07_Security_Specialist](.trae/skills/07_Security_Specialist/SKILL.md)**: 认证、GDPR 与安全需求。

### 🤖 08. AI Engineer (AI 工程师)
**目标**: 构建 LLM 应用。
- **[08_AI_Engineer](.trae/skills/08_AI_Engineer/SKILL.md)**: RAG 与 LangChain 架构。

### 📈 09. Operations & Growth (运营与增长)
**目标**: 提升用户增长与运营效率。
- **[09_Operations_Growth](.trae/skills/09_Operations_Growth/SKILL.md)**: 内容创作、数据分析与活动策划。

### 🌟 99. Meta Skills (元能力)
**目标**: 扩展与协作。
- **[99_Meta_SkillCreator](.trae/skills/99_Meta_SkillCreator/SKILL.md)**: 创建新的 Skills。
- **[99_Meta_Customization](.trae/skills/99_Meta_Customization/SKILL.md)**: 用户偏好设置与自定义配置指南。
- **[universal-dev-team](.trae/skills/universal-dev-team/SKILL.md)**: 全能开发团队编排器。

---

## 🛠️ 维护指南

本目录包含所有已整理的最佳实践技能。如需添加新技能，请参考 [99_Meta_SkillCreator](.trae/skills/99_Meta_SkillCreator/SKILL.md)。
