# fireworks-tech-graph

> 🎨 **AI/Agent 技术图表生成器** - 用自然语言描述你的系统，几秒钟得到可直接发布的 SVG + PNG 技术图。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![7 种视觉风格](https://img.shields.io/badge/风格-7种-purple)]()
[![14 种图类型](https://img.shields.io/badge/图类型-14种-green)]()
[![UML 完整支持](https://img.shields.io/badge/UML-完整支持-orange)]()

## ✨ 核心特性

- 🎯 **7 种视觉风格** - 从扁平图标到暗黑终端，从玻璃态到官方品牌风格
- 🤖 **AI/Agent 领域深度支持** - RAG、Agentic Search、Mem0、Multi-Agent、Tool Call 等常见 Pattern
- 📊 **14 种 UML 图类型** - 完整支持全部 UML 图（类图、序列图、状态机、ER 图等）
- 🔧 **语义形状词汇表** - LLM = 双边框圆角矩形，Agent = 六边形，Vector Store = 带内环圆柱
- 🎨 **语义箭头系统** - 颜色 + 虚线样式编码含义（写入/读取/异步/循环）
- 💾 **SVG + PNG 双输出** - SVG 可编辑，PNG 可直接嵌入文章

## 🚀 快速开始

### 安装

```bash
npx skills add yizhiyanhua-ai/fireworks-tech-graph
```

### 使用示例

```
用户: "画一张 Mem0 的架构图，暗黑风格"
  → Skill 识别：Memory Architecture Diagram，Style 2
  → 生成含泳道、圆柱体、语义箭头的 SVG
  → 导出 1920px PNG
  → 输出路径：mem0-architecture.svg / mem0-architecture.png
```

## 📋 支持的图类型

### AI/Agent 领域图
- **Agent Architecture** - Agent 推理循环、Tool Call 流程
- **Memory Architecture** - Mem0、MemGPT 风格记忆层次
- **RAG Pipeline** - 经典 RAG、Agentic RAG
- **Multi-Agent** - 多 Agent 协作编排

### UML 图（14 种）
- Class、Component、Deployment、Package、Composite Structure
- Object、Use Case、Activity、State Machine、Sequence
- Communication、Timing、Interaction Overview
- ER Diagram

### 其他技术图
- 架构图、数据流图、流程图
- 时序图、比较矩阵、时间线
- 思维导图、网络拓扑图

## 🎨 7 种视觉风格

| # | 风格 | 背景 | 最佳用途 |
|---|------|------|---------|
| 1 | **Flat Icon** | 白色 | 博客、文档、演示 |
| 2 | **Dark Terminal** | #0f0f1a | GitHub、技术文章 |
| 3 | **Blueprint** | #0a1628 | 架构文档 |
| 4 | **Notion Clean** | 白色,极简 | Notion 文档 |
| 5 | **Glassmorphism** | 深色渐变 | 产品网站、Keynote |
| 6 | **Claude Official** | 暖米色 #f8f6f3 | Anthropic 风格 |
| 7 | **OpenAI Official** | 纯白色 #ffffff | OpenAI 风格 |

## 📖 文档

- [📚 完整文档](README.zh.md) - 中文详细使用指南
- [📖 English Documentation](README.md) - English full documentation
- [📄 SKILL.md](SKILL.md) - Trae Skill 格式（用于导入）

## 🔧 技术栈

- SVG 生成（Python 脚本 + 模板）
- PNG 导出（cairosvg / rsvg-convert / puppeteer）
- 7 种风格系统（颜色、字体、背景、图标）

## 👨‍💻 作者

**Brad Zhang** - AI/Agent Infrastructure Builder

- 🌐 Website: https://bradzhang.dev
- 💼 Work with me: https://bradzhang.dev/en/work-with-me

## 📄 License

MIT License - 详见 [LICENSE](LICENSE)

---

**构建 AI 基础设施和开发工具？** 我开放合作讨论，包括付费冲刺、设计合作、创始工程师职位。
