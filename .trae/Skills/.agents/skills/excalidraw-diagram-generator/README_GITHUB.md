# excalidraw-diagram-generator

> ✏️ **手绘风格协作图表生成器** - 从自然语言描述生成 Excalidraw 图表，支持团队在线协作

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)]()
[![支持协作](https://img.shields.io/badge/协作-在线实时-green)]()
[![多种图类型](https://img.shields.io/badge/图类型-9种-purple)]()

## ✨ 核心特性

- 🎨 **手绘风格** - Excalidraw 标志性的手绘美学，适合快速原型和头脑风暴
- 👥 **在线协作** - 支持多人实时编辑，适合团队讨论
- ☁️ **云服务图标库** - 可添加 AWS、GCP、Azure 官方图标
- 📊 **9 种图类型** - 流程图、关系图、思维导图、架构图等
- 🔧 **Python 脚本工具** - 添加图标、箭头等辅助工具
- 📥 **.excalidraw 文件** - 可在 https://excalidraw.com 直接打开

## 🚀 快速开始

### 安装

```bash
# 通过 Trae 安装
npx skills add github/awesome-copilot/excalidraw-diagram-generator

# 或直接克隆
git clone https://github.com/awesome-copilot/excalidraw-diagram-generator.git
```

### 使用示例

```bash
# 1. 生成基础图表
# 用户: "创建用户注册登录的流程图"
# → 生成 user-registration.excalidraw 文件

# 2. 添加图标（可选）
python scripts/add-icon-to-diagram.py \
  my-diagram.excalidraw \
  EC2 \
  400 \
  300 \
  --label "Web Server"

# 3. 添加连接箭头
python scripts/add-arrow.py \
  my-diagram.excalidraw \
  300 250 \
  500 300 \
  --label "HTTPS"

# 4. 在浏览器中打开
open https://excalidraw.com
# 拖拽 .excalidraw 文件到页面
```

## 📋 支持的图类型

| 图类型 | 用途 | 模板文件 |
|--------|------|---------|
| **Flowchart** | 流程图、决策树 | `templates/flowchart-template.excalidraw` |
| **Relationship Diagram** | 实体关系图 | `templates/relationship-template.excalidraw` |
| **Mind Map** | 思维导图 | `templates/mindmap-template.excalidraw` |
| **Architecture Diagram** | 系统架构图 | - |
| **Data Flow Diagram** | 数据流图 | `templates/data-flow-diagram-template.excalidraw` |
| **Business Flow (Swimlane)** | 泳道图 | `templates/business-flow-swimlane-template.excalidraw` |
| **Class Diagram** | 类图 | `templates/class-diagram-template.excalidraw` |
| **Sequence Diagram** | 时序图 | `templates/sequence-diagram-template.excalidraw` |
| **ER Diagram** | ER 图 | `templates/er-diagram-template.excalidraw` |

## 🎯 典型场景

### 1. 快速原型
```
用户: "帮我画一个用户注册登录的流程图，要手绘风格"
↓
生成: user-registration.excalidraw
↓
打开: https://excalidraw.com
↓
团队协作编辑
```

### 2. 团队头脑风暴
```
Step 1: 生成基础思维导图
        "机器学习概念思维导图"

Step 2: 团队在 excalidraw.com 协作
        - 添加新分支
        - 修改布局
        - 讨论想法

Step 3: 导出最终版本
```

### 3. AWS 架构协作
```
Step 1: 安装 AWS 图标库
        访问 https://libraries.excalidraw.com/
        下载 AWS Architecture Icons

Step 2: 分割图标库
        python scripts/split-excalidraw-library.py \
          libraries/aws-icons/

Step 3: 生成架构图
        python scripts/add-icon-to-diagram.py \
          my-aws-diagram.excalidraw \
          "Internet-gateway" 150 100 \
          --label "Internet Gateway"

Step 4: 团队在 excalidraw.com 协作编辑
```

## 📁 项目结构

```
excalidraw-diagram-generator/
├── SKILL.md                                 # Trae Skill 定义
├── references/
│   ├── excalidraw-schema.md               # Excalidraw JSON Schema
│   └── element-types.md                    # 元素类型规范
├── templates/                              # 模板文件
│   ├── flowchart-template.excalidraw
│   ├── relationship-template.excalidraw
│   ├── mindmap-template.excalidraw
│   ├── data-flow-diagram-template.excalidraw
│   ├── business-flow-swimlane-template.excalidraw
│   ├── class-diagram-template.excalidraw
│   ├── sequence-diagram-template.excalidraw
│   └── er-diagram-template.excalidraw
├── scripts/                               # Python 工具脚本
│   ├── add-icon-to-diagram.py            # 添加图标
│   ├── add-arrow.py                      # 添加箭头
│   └── split-excalidraw-library.py       # 分割图标库
└── README_GITHUB.md                      # GitHub 文档
```

## 🔧 Python 工具脚本

### 添加图标

```bash
python scripts/add-icon-to-diagram.py \
  <diagram.excalidraw> \
  <icon-name> \
  <x> \
  <y> \
  [--label "Label Text"] \
  [--library-path PATH]
```

**示例**:
```bash
# 添加 EC2 图标
python scripts/add-icon-to-diagram.py \
  my-diagram.excalidraw \
  EC2 \
  400 \
  300 \
  --label "Web Server"

# 从自定义图标库添加
python scripts/add-icon-to-diagram.py \
  my-diagram.excalidraw \
  Compute-Engine \
  500 \
  200 \
  --library-path libraries/gcp-icons \
  --label "API Server"
```

### 添加箭头

```bash
python scripts/add-arrow.py \
  <diagram.excalidraw> \
  <from-x> \
  <from-y> \
  <to-x> \
  <to-y> \
  [--label "Arrow Label"] \
  [--style solid|dashed|dotted] \
  [--color "#7950f2"]
```

**示例**:
```bash
# 简单箭头
python scripts/add-arrow.py \
  my-diagram.excalidraw \
  300 250 \
  500 300

# 带标签的虚线箭头
python scripts/add-arrow.py \
  my-diagram.excalidraw \
  400 350 \
  600 400 \
  --label "HTTPS" \
  --style dashed \
  --color "#7950f2"
```

### 分割图标库

```bash
python scripts/split-excalidraw-library.py \
  <library-directory>
```

**示例**:
```bash
# 分割 AWS 图标库
python scripts/split-excalidraw-library.py \
  libraries/aws-architecture-icons/
```

**输出结构**:
```
libraries/aws-architecture-icons/
├── aws-architecture-icons.excalidrawlib  # 原始文件
├── reference.md                        # 图标查找表
└── icons/                              # 分割后的图标
    ├── API-Gateway.json
    ├── CloudFront.json
    ├── EC2.json
    ├── Lambda.json
    ├── RDS.json
    └── S3.json
```

## 📦 设置图标库

### 安装流程

1. **下载图标库**
   - 访问 https://libraries.excalidraw.com/
   - 搜索并下载图标库（如 AWS Architecture Icons）

2. **创建目录**
   ```bash
   mkdir -p libraries/aws-architecture-icons
   ```

3. **放置文件**
   ```bash
   mv ~/Downloads/aws-icons.excalidrawlib \
      libraries/aws-architecture-icons/
   ```

4. **分割图标库**
   ```bash
   python scripts/split-excalidraw-library.py \
     libraries/aws-architecture-icons/
   ```

5. **验证**
   ```bash
   ls libraries/aws-architecture-icons/icons/
   ```

### 支持的图标库

- Cloud service icons (AWS, GCP, Azure)
- Kubernetes / infrastructure icons
- UI / Material icons
- Flowchart / diagram symbols
- Network diagram icons

## 🎨 最佳实践

### 元素数量指南

| 图类型 | 推荐数量 | 最大数量 |
|--------|---------|---------|
| Flowchart 步骤 | 3-10 | 15 |
| Relationship 实体 | 3-8 | 12 |
| Mind Map 分支 | 4-6 | 8 |
| Mind Map 子主题 | 2-4 | 6 |

### 布局技巧

1. **起始位置**: 重要元素居中，使用一致的间距
2. **间距**:
   - 水平间距: 200-300px
   - 垂直间距: 100-150px
3. **颜色**: 使用一致的配色方案
   - 主元素: 浅蓝色 `#a5d8ff`
   - 次要元素: 浅绿色 `#b2f2bb`
   - 重要/中心: 黄色 `#ffd43b`
   - 警告: 浅红色 `#ffc9c9`
4. **字体**: 16-24px 确保可读性
5. **字体**: **所有文本必须使用 `fontFamily: 5`（Excalifont）**

### 复杂度管理

如果图表太复杂：
- 建议拆分成多个图表
- 先聚焦主要元素
- 提供创建详细子图的选项

## 🔍 故障排除

| 问题 | 解决方案 |
|------|---------|
| 元素重叠 | 增加坐标间距 |
| 文本不适合框 | 增加框宽度或减小字体 |
| 太多元素 | 拆分成多个图表 |
| 布局不清晰 | 使用网格布局或径向布局 |
| 颜色不一致 | 先定义配色方案 |

## 📚 文档

- [📄 SKILL.md](SKILL.md) - Trae Skill 格式定义
- [📖 Excalidraw Schema](references/excalidraw-schema.md) - JSON Schema 文档
- [🎨 Element Types](references/element-types.md) - 元素类型规范

## 🤝 协作流程

```
1. 生成基础图表
   └── Agent 生成 .excalidraw 文件

2. 分享文件
   └── 用户下载或复制文件路径

3. 在线协作
   └── 访问 https://excalidraw.com
   └── 拖拽文件或点击 Open
   └── 邀请团队成员

4. 导出最终版本
   └── PNG / SVG / PDF 导出
```

## 📄 License

MIT License

## 🔗 相关资源

- [Excalidraw](https://excalidraw.com) - 在线绘图工具
- [Excalidraw Libraries](https://libraries.excalidraw.com/) - 图标库下载
- [fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) - AI/Agent 专用图表
- [architecture-diagram](https://github.com/cocoon-ai/architecture-diagram) - 深色主题架构图

---

**提示**: 使用 fireworks-tech-graph 生成 AI/Agent 技术图，使用 architecture-diagram 生成深色专业架构图，使用本 Skill 生成手绘协作图表。
