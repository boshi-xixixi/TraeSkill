# architecture-diagram

> 🎨 **专业深色主题架构图生成器** - 一键生成云架构、Kubernetes、安全架构图，支持导出 PNG/PDF

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)]()
[![导出格式](https://img.shields.io/badge/导出-HTML+SVG+PNG+PDF-green)]()
[![深色主题](https://img.shields.io/badge/主题-深色专业-purple)]()

## ✨ 核心特性

- 🌙 **深色专业主题** - 专为技术文档、技术演讲、深色模式设计的视觉风格
- ☁️ **云架构支持** - AWS、GCP、Azure 架构图
- 🔒 **安全架构** - 防火墙、VPC、认证流程
- ☸️ **Kubernetes** - Pod 部署、Service Mesh、Ingress
- 📊 **语义化设计系统** - Frontend/Backend/Database/Security 组件类型化
- 📋 **一键导出** - Copy PNG / Download PNG / Download PDF

## 🚀 快速开始

### 安装

```bash
# 通过 Trae 安装
npx skills add github/cocoon-ai/architecture-diagram

# 或直接克隆
git clone https://github.com/cocoon-ai/architecture-diagram.git
```

### 使用示例

```bash
# 创建 AWS 微服务架构图
# 1. 复制 template.html
cp resources/template.html my-architecture.html

# 2. 修改内容
# - 更新标题和描述
# - 添加组件框（Frontend、Backend、Database）
# - 绘制连接箭头
# - 自定义图例

# 3. 在浏览器中打开
open my-architecture.html

# 4. 使用导出工具栏
# 点击 ⋯ 按钮 → 📋 Copy / 🖼️ PNG / 📄 PDF
```

## 📖 设计系统

### 语义化颜色

| 组件类型 | 填充色 (rgba) | 描边色 |
|---------|-------------|--------|
| Frontend | `rgba(8, 51, 68, 0.4)` | `#22d3ee` (青色) |
| Backend | `rgba(6, 78, 59, 0.4)` | `#34d399` (翠绿) |
| Database | `rgba(76, 29, 149, 0.4)` | `#a78bfa` (紫罗兰) |
| AWS/Cloud | `rgba(120, 53, 15, 0.3)` | `#fbbf24` (琥珀) |
| Security | `rgba(136, 19, 55, 0.4)` | `#fb7185` (玫瑰) |
| Message Bus | `rgba(251, 146, 60, 0.3)` | `#fb923c` (橙色) |
| External | `rgba(30, 41, 59, 0.5)` | `#94a3b8` (板岩) |

### 视觉元素

- **背景**: `#020617` (slate-950) + 网格图案
- **组件框**: 圆角矩形 `rx="6"`，1.5px 描边
- **安全组**: 虚线描边 `stroke-dasharray="4,4"`
- **区域边界**: 更大的虚线 `stroke-dasharray="8,4"`
- **字体**: JetBrains Mono（等宽，技术美学）

## 🎯 典型场景

### 1. 云架构图
```
┌─────────────────────────────────────────────┐
│  AWS / GCP / Azure                          │
│  ┌──────────┐    ┌──────────┐             │
│  │ Frontend │───▶│  Backend │            │
│  └──────────┘    └──────────┘            │
│                      │                    │
│                      ▼                    │
│              ┌──────────────┐             │
│              │   Database   │            │
│              └──────────────┘             │
└─────────────────────────────────────────────┘
```

### 2. Kubernetes 架构
```
┌─────────────────────────────────────────────┐
│  Kubernetes Cluster                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐   │
│  │  Pod 1  │  │  Pod 2  │  │  Pod 3  │   │
│  └─────────┘  └─────────┘  └─────────┘   │
│       │                              │     │
│       └───────── Service ─────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │           Ingress Controller         │   │
│  └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

### 3. 安全架构
```
┌─────────────────────────────────────────────┐
│  Security Architecture                      │
│  ┌──────────┐                              │
│  │ Firewall │                             │
│  └────┬─────┘                             │
│       │                                    │
│  ┌────▼─────┐    ┌──────────────────┐    │
│  │   VPN    │───▶│  Auth Service     │    │
│  └──────────┘    └──────────────────┘    │
└─────────────────────────────────────────────┘
```

## 📁 项目结构

```
architecture-diagram/
├── SKILL.md                    # Trae Skill 定义
├── resources/
│   └── template.html          # HTML 模板
└── README_GITHUB.md           # GitHub 文档
```

## 🛠️ 工具栏功能

每个生成的 HTML 文件都内置导出工具栏：

| 按钮 | 功能 | 说明 |
|------|------|------|
| 📋 Copy | 复制到剪贴板 | 高 DPI PNG (scale: 2) |
| 🖼️ PNG | 下载 PNG | 高 DPI PNG 下载 |
| 📄 PDF | 下载 PDF | 嵌入深色主题 PDF |

**使用方式**:
1. 在浏览器中打开生成的 HTML 文件
2. 点击右上角的 `⋯` 按钮
3. 选择导出格式

## 🔧 自定义

### 修改组件框

```svg
<rect x="X" y="Y" width="W" height="H" rx="6"
      fill="rgba(8, 51, 68, 0.4)"
      stroke="#22d3ee"
      stroke-width="1.5"/>
<text x="CENTER_X" y="Y+20"
      fill="white"
      font-size="11"
      font-weight="600"
      text-anchor="middle">LABEL</text>
```

### 修改连接箭头

```svg
<marker id="arrowhead"
        markerWidth="10"
        markerHeight="7"
        refX="9"
        refY="3.5"
        orient="auto">
  <polygon points="0 0, 10 3.5, 0 7" fill="#64748b" />
</marker>

<line x1="startX" y1="startY"
      x2="endX" y2="endY"
      stroke="#64748b"
      marker-end="url(#arrowhead)"/>
```

## 📚 文档

- [📄 SKILL.md](SKILL.md) - Trae Skill 格式定义
- [🎨 模板](resources/template.html) - 可直接修改使用

## 👨‍💻 作者

**Cocoon AI** - hello@cocoon-ai.com

## 📄 License

MIT License

---

**提示**: 使用 [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) 生成 AI/Agent 架构图，使用本 Skill 生成专业深色主题架构图。
