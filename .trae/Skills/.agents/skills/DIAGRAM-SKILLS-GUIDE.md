# 图表生成 Skill 搭配指南

> 本文档说明 TraeSkill 中三个图表生成 Skill 的最佳使用场景和搭配策略。

## 📋 Skill 概览

已安装的三个图表生成 Skill：

| Skill | 定位 | 输出格式 | 核心优势 |
|-------|------|---------|---------|
| **fireworks-tech-graph** | 🏆 通用技术图表 | SVG + PNG | 14种 UML、AI/Agent 架构、7种风格 |
| **architecture-diagram** | 🎨 专业深色架构 | HTML + SVG + PNG + PDF | 深色主题、内置导出工具栏 |
| **excalidraw-diagram-generator** | ✏️ 手绘协作图表 | .excalidraw JSON | 手绘风格、在线协作、图标库 |

---

## 🎯 场景化选择决策树

```
开始
  ↓
这是 AI/Agent/LLM 相关图表吗？
  ├─ 是 → fireworks-tech-graph ⭐
  │     (Agent Loop、Memory、Tool Call、RAG)
  │     ↓
  │     需要深色专业主题吗？
  │       ├─ 是 → fireworks-tech-graph (Style 2: Dark Terminal)
  │       └─ 否 → fireworks-tech-graph (任意风格)
  │
  └─ 否 → 继续 ↓
         ↓
         这是云架构/基础设施图吗？
           ├─ 是 → architecture-diagram (深色主题)
           │     ↓
           │     需要在线协作或手绘风格吗？
           │       ├─ 是 → excalidraw-diagram-generator
           │       └─ 否 → architecture-diagram
           │
           └─ 否 → 继续 ↓
                  ↓
                  需要团队在线编辑协作吗？
                    ├─ 是 → excalidraw-diagram-generator
                    │     (打开 https://excalidraw.com 在线协作)
                    │
                    └─ 否 → fireworks-tech-graph (默认首选)
                          ↓
                          需要特定 UML 图类型吗？
                            ├─ Class/Object → fireworks-tech-graph
                            ├─ Sequence → fireworks-tech-graph
                            ├─ State Machine → fireworks-tech-graph
                            ├─ ER Diagram → fireworks-tech-graph
                            ├─ Use Case → fireworks-tech-graph
                            ├─ Component → fireworks-tech-graph
                            └─ Deployment → fireworks-tech-graph 或 architecture-diagram
```

---

## 🏆 fireworks-tech-graph（第一优先级）

### 核心场景

1. **AI/Agent 系统架构** ⭐⭐⭐
   - Agent Reasoning Loop
   - Memory Architecture (Mem0, MemGPT)
   - Tool Call 流程
   - Multi-Agent Orchestration
   - Agentic RAG

2. **RAG 系统图表** ⭐⭐⭐
   - 经典 RAG Pipeline
   - Agentic RAG
   - RAG Fusion
   - Hybrid Search

3. **完整 UML 图支持** ⭐⭐⭐
   - Class Diagram
   - Sequence Diagram
   - State Machine Diagram
   - ER Diagram
   - Use Case Diagram
   - Activity Diagram

4. **数据流/架构图** ⭐⭐⭐
   - 微服务架构
   - 事件驱动架构
   - 消息队列架构
   - ETL Pipeline

### 7 种视觉风格

| # | 风格名称 | 背景色 | 最佳用途 |
|---|---------|--------|---------|
| 1 | **Flat Icon** | 白色 | 博客、文档、演示 |
| 2 | **Dark Terminal** | #0f0f1a | GitHub、技术文章 |
| 3 | **Blueprint** | #0a1628 | 架构文档 |
| 4 | **Notion Clean** | 白色,极简 | Notion 文档 |
| 5 | **Glassmorphism** | 深色渐变 | 产品网站、Keynote |
| 6 | **Claude Official** | 暖米色 #f8f6f3 | Anthropic 风格 |
| 7 | **OpenAI Official** | 纯白色 #ffffff | OpenAI 风格 |

### 使用示例

**示例 1: Agent Loop 架构**
```
用户请求: "帮我画一个 Agent 的推理循环架构图"
Skill 选择: fireworks-tech-graph
推荐风格: Style 6 (Claude Official)
图类型: Agent Architecture Diagram
```

**示例 2: RAG Pipeline**
```
用户请求: "画出完整的 RAG 系统数据流图"
Skill 选择: fireworks-tech-graph
推荐风格: Style 2 (Dark Terminal)
图类型: Data Flow Diagram
```

---

## 🎨 architecture-diagram（第二优先级）

### 核心场景

1. **云服务架构** ⭐⭐⭐
   - AWS 架构图
   - GCP 架构图
   - Azure 架构图

2. **Kubernetes 架构** ⭐⭐⭐
   - Pod 部署
   - Service Mesh
   - Ingress 配置

3. **网络安全架构** ⭐⭐
   - 防火墙规则
   - VPC 配置
   - 认证流程

4. **深色主题文档** ⭐⭐
   - 深色模式技术博客
   - 技术演讲 PPT
   - 深色主题幻灯片

### 内置功能

✅ **一键导出工具栏**
- 📋 Copy (高 DPI PNG 剪贴板)
- 🖼️ PNG (高 DPI 下载)
- 📄 PDF (嵌入深色主题)

✅ **专业设计系统**
- 语义化颜色（Frontend/Backend/Database/Security）
- JetBrains Mono 字体
- 网格背景
- 组件语义化设计

### 使用示例

**示例 1: AWS 微服务架构**
```
用户请求: "画一个 AWS 上的微服务架构图，包含 API Gateway、Lambda、DynamoDB"
Skill 选择: architecture-diagram
推荐: 深色主题（内置）
```

**示例 2: Kubernetes 部署架构**
```
用户请求: "展示 Kubernetes 集群的部署架构，包含 Ingress、Service、Pod"
Skill 选择: architecture-diagram
推荐: 深色主题（内置）
```

---

## ✏️ excalidraw-diagram-generator（第三优先级）

### 核心场景

1. **快速原型/头脑风暴** ⭐⭐⭐
   - 快速草图想法
   - 概念可视化
   - 流程草图

2. **团队协作编辑** ⭐⭐⭐
   - 在线实时协作
   - 客户沟通
   - 演示讨论

3. **云服务图标图** ⭐⭐
   - AWS 架构（带官方图标）
   - GCP 架构（带官方图标）
   - Azure 架构（带官方图标）

4. **业务流程图** ⭐⭐
   - 用户旅程图
   - 业务流程
   - 泳道图

### 使用流程

1. **生成 .excalidraw 文件**
2. **打开方式**：
   - 访问 https://excalidraw.com
   - 点击 "Open" 或拖拽文件
   - 或使用 VS Code Excalidraw 扩展

3. **可选：添加图标库**
   ```bash
   # 下载图标库
   访问 https://libraries.excalidraw.com/
   搜索并下载 AWS/GCP/Azure 图标库

   # 使用 Python 脚本添加图标
   python scripts/add-icon-to-diagram.py <file> <icon-name> <x> <y>
   ```

### 使用示例

**示例 1: 快速流程图**
```
用户请求: "帮我画一个用户注册登录的流程图，要手绘风格"
Skill 选择: excalidraw-diagram-generator
输出: .excalidraw 文件 → 在 excalidraw.com 打开编辑
```

**示例 2: 团队协作架构图**
```
用户请求: "我们团队要一起画一个 AWS 架构图，要用 AWS 官方图标"
Skill 选择: excalidraw-diagram-generator
设置: 先安装 AWS Architecture Icons 图标库
输出: .excalidraw 文件 → 团队在 excalidraw.com 协作
```

---

## 🔄 高级工作流：组合使用

### 场景 1: 从草图到生产图

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

### 场景 2: AI/Agent 深度分析

```
用户: "我想可视化一个 Agent 系统，包括 Memory、Tools、Reasoning"

Step 1: fireworks-tech-graph
- 图类型: Agent Architecture
- 输出: Agent Loop 架构图 (SVG)
- 风格: Claude Official 或 Dark Terminal

Step 2: fireworks-tech-graph
- 图类型: Sequence Diagram
- 输出: Tool Call 时序图 (SVG)

Step 3: fireworks-tech-graph
- 图类型: Memory Architecture
- 输出: Memory 层次结构图 (SVG)

最终交付: 3 个专业 SVG 图表
```

### 场景 3: 云架构协作

```
Step 1: excalidraw-diagram-generator
- 快速草图 AWS 架构
- 团队在 excalidraw.com 讨论
- 添加 AWS 图标

Step 2: architecture-diagram
- 根据讨论结果创建专业深色主题图
- 输出: HTML + 一键导出 PNG/PDF

最终交付: 专业深色主题云架构图 + 协作源文件
```

---

## 📊 快速参考表

| 需求 | 推荐 Skill | 理由 |
|------|-----------|------|
| Agent Loop 架构 | fireworks-tech-graph | 深度支持 AI 概念 |
| RAG Pipeline | fireworks-tech-graph | 完整 RAG 模式支持 |
| Memory 系统图 | fireworks-tech-graph | 专门的 Memory 图类型 |
| UML Class 图 | fireworks-tech-graph | 完整 UML 符号 |
| Sequence 时序图 | fireworks-tech-graph | 支持 alt/opt/loop 帧 |
| ER 数据库图 | fireworks-tech-graph | Chen 符号支持 |
| AWS 架构图（深色） | architecture-diagram | 专业深色主题 |
| K8s 部署图 | architecture-diagram | 云原生架构 |
| 安全架构图 | architecture-diagram | 语义化 Security 颜色 |
| 快速草图 | excalidraw-diagram-generator | 手绘风格 |
| 团队在线协作 | excalidraw-diagram-generator | 支持多人实时编辑 |
| 带云图标架构 | excalidraw-diagram-generator | AWS/GCP/Azure 图标库 |
| 深色博客图 | fireworks-tech-graph (Style 2) | Dark Terminal 风格 |
| 技术演讲 PPT | fireworks-tech-graph (Style 6) | Claude 风格 |
| 产品 Keynote | fireworks-tech-graph (Style 5) | Glassmorphism 风格 |

---

## 🎓 最佳实践

### 1. 从 fireworks-tech-graph 开始
- 这是最通用的工具
- 支持 14 种图类型
- 覆盖 95% 的技术图表需求

### 2. 按需升级到专业工具
- 需要深色主题 → architecture-diagram
- 需要协作/手绘 → excalidraw-diagram-generator

### 3. 不要混合风格
- 每个图表只用一个工具
- 保持视觉一致性

### 4. 善用 Style 选择
- 博客/文档 → Flat Icon (Style 1)
- 技术文章 → Dark Terminal (Style 2)
- 架构文档 → Blueprint (Style 3)
- Anthropic 风格 → Claude Official (Style 6)
- OpenAI 风格 → OpenAI Official (Style 7)

### 5. 验证和迭代
- fireworks-tech-graph: 使用 `validate-svg.sh` 验证
- architecture-diagram: 使用内置导出工具栏
- excalidraw-diagram-generator: 在 excalidraw.com 预览

---

## 🚀 安装位置

所有三个 Skill 已安装到：

```
/Users/lishibo/code/GitHub/TraeSkill/.trae/skills/.agents/skills/
├── fireworks-tech-graph/      # SVG 通用图表生成器
├── architecture-diagram/       # HTML 深色架构图
└── excalidraw-diagram-generator/  # 手绘协作图表
```

---

## 📚 相关文档

- [fireworks-tech-graph README.md](fireworks-tech-graph/README.md)
- [architecture-diagram SKILL.md](architecture-diagram/SKILL.md)
- [excalidraw-diagram-generator SKILL.md](excalidraw-diagram-generator/SKILL.md)

---

**版本**: 1.0.0  
**更新**: 2026-05-12  
**维护**: TraeSkill Team
