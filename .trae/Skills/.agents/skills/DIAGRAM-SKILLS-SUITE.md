# 🎨 TraeSkill 图表生成 Skill 套件

> 本仓库包含三个互补的图表生成 Skill，覆盖 95%+ 的技术图表需求。

## 📦 包含的 Skills

### 1. 🎯 fireworks-tech-graph
**通用技术图表生成器**

- **输出**: SVG + PNG
- **核心优势**: AI/Agent 架构、14 种 UML、7 种视觉风格
- **安装**: `npx skills add yizhiyanhua-ai/fireworks-tech-graph`
- **GitHub**: https://github.com/yizhiyanhua-ai/fireworks-tech-graph

**最佳场景**:
- Agent Loop 架构图
- RAG Pipeline
- Memory 系统图
- 完整 UML 图支持
- 技术博客/文档

### 2. 🎨 architecture-diagram
**专业深色主题架构图**

- **输出**: HTML + SVG + PNG + PDF
- **核心优势**: 深色主题、一键导出、专业设计系统
- **安装**: `npx skills add github/cocoon-ai/architecture-diagram`
- **GitHub**: https://github.com/cocoon-ai/architecture-diagram

**最佳场景**:
- AWS/GCP/Azure 架构图
- Kubernetes 部署图
- 安全架构图
- 深色主题技术演讲

### 3. ✏️ excalidraw-diagram-generator
**手绘风格协作图表**

- **输出**: .excalidraw JSON
- **核心优势**: 手绘风格、在线协作、云服务图标
- **安装**: `npx skills add github/awesome-copilot/excalidraw-diagram-generator`
- **GitHub**: https://github.com/awesome-copilot/excalidraw-diagram-generator

**最佳场景**:
- 快速原型/头脑风暴
- 团队在线协作
- 客户演示沟通
- 带云图标架构图

## 🔄 选择决策树

```
开始
  ↓
这是 AI/Agent 相关图表吗？
  ├─ 是 → fireworks-tech-graph ⭐
  │     (Agent Loop、Memory、Tool Call、RAG)
  │
  └─ 否 → 继续 ↓
         ↓
         需要深色专业主题吗？
           ├─ 是 → architecture-diagram
           │     (云架构、Kubernetes、安全)
           │
           └─ 否 → 继续 ↓
                  ↓
                  需要在线协作/手绘风格吗？
                    ├─ 是 → excalidraw-diagram-generator
                    │     (团队协作、快速原型)
                    │
                    └─ 否 → fireworks-tech-graph (默认)
```

## 📊 功能对比

| 维度 | fireworks-tech-graph | architecture-diagram | excalidraw |
|------|---------------------|---------------------|-------------|
| **输出格式** | SVG + PNG | HTML + PNG + PDF | .excalidraw |
| **视觉风格** | 7 种专业风格 | 深色主题（内置） | 手绘/草图 |
| **UML 支持** | 14 种完整类型 | 仅架构图 | 8 种类型 |
| **AI/Agent 场景** | ✅ 深度支持 | ❌ 不支持 | ❌ 不支持 |
| **协作能力** | ❌ 静态输出 | ❌ 静态输出 | ✅ 在线编辑 |
| **云服务图标** | ❌ 手动 SVG | ❌ 手动 SVG | ✅ 支持库 |
| **适用人群** | 开发者、技术写作者 | 架构师、DevOps | 设计师、团队 |

## 🚀 使用示例

### 示例 1: AI Agent 系统可视化
```
用户: "帮我画一个 Agent 的推理循环架构图"

Skill 选择: fireworks-tech-graph
图类型: Agent Architecture Diagram
风格: Claude Official 或 Dark Terminal
输出: agent-loop.svg + agent-loop.png
```

### 示例 2: AWS 云架构文档
```
用户: "画一个 AWS 微服务架构图，要深色主题"

Skill 选择: architecture-diagram
输出: aws-architecture.html
使用: 一键导出 PNG/PDF
```

### 示例 3: 团队协作头脑风暴
```
用户: "我们团队要一起画一个 AWS 架构图"

Skill 选择: excalidraw-diagram-generator
图标库: AWS Architecture Icons
协作: https://excalidraw.com 在线编辑
```

## 🔧 独立使用

每个 Skill 都可以独立使用：

```bash
# fireworks-tech-graph
npx skills add yizhiyanhua-ai/fireworks-tech-graph

# architecture-diagram
npx skills add github/cocoon-ai/architecture-diagram

# excalidraw-diagram-generator
npx skills add github/awesome-copilot/excalidraw-diagram-generator
```

## 📚 文档

- [fireworks-tech-graph README](fireworks-tech-graph/README_GITHUB.md)
- [architecture-diagram README](architecture-diagram/README_GITHUB.md)
- [excalidraw-diagram-generator README](excalidraw-diagram-generator/README_GITHUB.md)
- [使用指南](DIAGRAM-SKILLS-GUIDE.md)

## 🤝 组合使用

### 场景: 从草图到生产图

```
excalidraw-diagram-generator (快速原型)
  ↓ 团队协作讨论
  ↓ 生成概念草图
  ↓
fireworks-tech-graph (生产级图表)
  ↓ 转换为专业 SVG
  ↓ 选择合适风格
  ↓
architecture-diagram (可选：深色主题)
  ↓ 如需深色专业输出
  ↓ 转换或重新设计
```

## 📋 Skill 特性矩阵

| Skill | AI/Agent | UML | 云架构 | 深色主题 | 在线协作 | 导出格式 |
|-------|-----------|-----|--------|----------|----------|----------|
| fireworks-tech-graph | ✅ 深度 | ✅ 14种 | ⚠️ 基础 | ✅ 7种 | ❌ | SVG/PNG |
| architecture-diagram | ❌ | ❌ | ✅ 专业 | ✅ 内置 | ❌ | HTML/PNG/PDF |
| excalidraw | ❌ | ⚠️ 8种 | ⚠️ 需图标库 | ❌ | ✅ | .excalidraw |

## 🎯 推荐场景速查表

| 需求 | 推荐 Skill | 理由 |
|------|-----------|------|
| Agent Loop 架构 | fireworks-tech-graph | 深度支持 AI 概念 |
| RAG Pipeline | fireworks-tech-graph | 完整 RAG 模式支持 |
| Memory 系统图 | fireworks-tech-graph | 专门的 Memory 图类型 |
| UML Class 图 | fireworks-tech-graph | 完整 UML 符号 |
| AWS 架构图（深色） | architecture-diagram | 专业深色主题 |
| K8s 部署图 | architecture-diagram | 云原生架构 |
| 安全架构图 | architecture-diagram | 语义化 Security 颜色 |
| 快速草图 | excalidraw-diagram-generator | 手绘风格 |
| 团队在线协作 | excalidraw-diagram-generator | 支持多人实时编辑 |
| 带云图标架构 | excalidraw-diagram-generator | AWS/GCP/Azure 图标库 |

## 📦 安装方式

所有三个 Skill 都已预装在 [TraeSkill](https://github.com/lishibo/TraeSkill) 项目中。

如需单独使用：

```bash
# fireworks-tech-graph
npx skills add yizhiyanhua-ai/fireworks-tech-graph

# architecture-diagram
npx skills add github/cocoon-ai/architecture-diagram

# excalidraw-diagram-generator
npx skills add github/awesome-copilot/excalidraw-diagram-generator
```

## 📄 License

MIT License

## 🙏 致谢

- [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) by Brad Zhang
- [architecture-diagram](https://github.com/cocoon-ai/architecture-diagram) by Cocoon AI
- [excalidraw-diagram-generator](https://github.com/awesome-copilot/excalidraw-diagram-generator) by awesome-copilot

## 🔗 相关资源

- [TraeSkill](https://github.com/lishibo/TraeSkill) - Trae AI Skill 集合
- [Excalidraw](https://excalidraw.com) - 在线绘图工具
- [Excalidraw Libraries](https://libraries.excalidraw.com/) - 图标库
- [Trae](https://trae.ai) - AI Code Assistant

---

**构建 AI 基础设施和开发工具？** 欢迎讨论合作，包括付费冲刺、设计合作、创始工程师职位。
