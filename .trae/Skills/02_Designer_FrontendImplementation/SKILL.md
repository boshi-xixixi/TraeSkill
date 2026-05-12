---
name: frontend-design
description: 当用户需要构建网页组件、页面、应用程序或任何 Web UI（网站、着陆页、仪表板、React 组件、HTML/CSS 布局）时使用。此 Skill 生成独特、生产级的前端界面，注重高质量设计和避免通用 AI 风格。
license: Complete terms in LICENSE.txt
---

> **⚠️ 性能提示**: 此 Skill 专注于设计理念和美学规范，不包含具体的实现代码。设计阶段完成后，配合 ReactBestPractices Skill 进行性能优化。

---

## 核心设计理念：拒绝 AI 塑料感

### 什么是"AI 塑料感"？

AI 生成的界面往往呈现出一致的"塑料感"特征：过度使用的字体、无特色的配色、可预测的布局。这些特征让界面看起来"正确"但毫无灵魂。

**核心原则**：每个设计都应该有**明确的美学观点**，而不是通用的"AI 风格"。

### 必须避免的"AI 塑料感"特征

| 反模式 | 问题 | 替代方案 |
|--------|------|---------|
| **过度使用的字体** | Arial, Inter, Roboto | 选择独特字体：JetBrains Mono, Playfair Display, Space Grotesk |
| **陈腐的配色** | #4F46E5 (蓝紫), 彩虹渐变 | 建立有性格的调色板：单色主导 + 锐利点缀色 |
| **可预测的布局** | 12 栏网格、卡片墙、英雄区 + 功能区 | 不对称、意外的空間构图、大胆的负空间 |
| **通用的动效** | 淡入淡出、基本悬停效果 | 意图明确的微交互、高影响时刻的动画 |
| **缺乏深度** | 纯色背景、无纹理 | 大气背景、微妙渐变、情境细节 |

---

## 设计思维框架（Design Before Code）

在编写任何代码之前，必须建立**大胆的美学方向**：

### 四个核心问题

```
1. PURPOSE（目的）
   - 这个界面解决什么问题？
   - 目标用户是谁？
   - 用户的情感需求是什么？

2. TONE（调性）
   选择一个大胆的美学方向：
   - 极简主义（Minimalist）
   - 极繁主义（Maximalist）
   - 复古未来主义（Retro-Futuristic）
   - 粗犷主义（Brutalist）
   - 有机自然（Organic）
   - 科技感（Tech/Cyberpunk）
   - 手工质感（Handcrafted）

3. CONSTRAINTS（限制）
   - 技术限制（浏览器支持、性能要求）
   - 品牌规范（如果有）
   - 无障碍要求（WCAG 等级）

4. DIFFERENTIATION（独特性）
   - 什么让这个设计令人难忘？
   - 用户离开后会记得什么？
   - 有什么意想不到的元素？
```

**CRITICAL**: 选择一个清晰的概念方向并精确执行。大胆的极繁主义和精致的极简主义都可以——关键是意图明确，而非强度高低。

---

## 前端美学五大支柱

### 1. 排版（Typography）

**核心原则**: 字体是设计的声音，选择要有意图

```css
/* ❌ 避免：过度使用的字体 */
font-family: 'Inter', 'Roboto', 'Arial', sans-serif;

/* ✅ 推荐：独特的字体组合 */
/* 科技感 */
font-family: 'JetBrains Mono', 'Fira Code', monospace;

/* 优雅感 */
font-family: 'Playfair Display', 'Cormorant Garamond', serif;

/* 现代感 */
font-family: 'Space Grotesk', 'DM Sans', sans-serif;

/* 实验性 */
font-family: 'Archivo Black', 'Bebas Neue', sans-serif;
```

**排版层次**:

- 使用 2-3 种字体（标题 + 正文 + 可选的 accent）
- 建立明确的字体大小阶梯（使用 `clamp()` 实现响应式）
- 字重对比强烈（400 vs 700+）
- 行高有呼吸感（1.5-1.75 用于正文）

### 2. 色彩与主题（Color & Theme）

**核心原则**: 凝聚的调色板，主导色 + 锐利点缀色

```css
/* ❌ 避免：AI 通用配色 */
--primary: #4F46E5; /* 无处不在的紫蓝色 */
--gradient: linear-gradient(to right, #667eea, #764ba2);

/* ✅ 推荐：有性格的调色板 */

/* 暗黑科技风 */
:root {
  --bg-primary: #0a0a0a;
  --bg-secondary: #141414;
  --text-primary: #fafafa;
  --accent: #22d3ee; /* 青色点缀 */
  --accent-glow: rgba(34, 211, 238, 0.3);
}

/* 温暖自然风 */
:root {
  --bg-primary: #faf8f5;
  --bg-secondary: #f0ebe3;
  --text-primary: #2d2a26;
  --accent: #e07a5f; /* 陶土橙 */
  --accent-muted: #f4a261;
}

/* 高对比极简风 */
:root {
  --bg-primary: #ffffff;
  --text-primary: #000000;
  --accent: #ff3366;
}
```

### 3. 动效与交互（Motion）

**核心原则**: 动画要有意图，聚焦高影响时刻

```css
/* ✅ 推荐：精心设计的动效 */
.page-load {
  animation: stagger-reveal 0.6s ease-out forwards;
  animation-delay: calc(var(--index) * 100ms);
}

/* ✅ 悬停效果要有惊喜 */
.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
}

/* ❌ 避免：通用淡入淡出 */
.fade-in {
  animation: fadeIn 0.3s ease-in-out;
}
```

**动效最佳实践**:
- 一个精心编排的页面加载动画比分散的微交互更令人愉悦
- 使用滚动触发和悬停状态带来惊喜
- 优先使用 CSS-only 解决方案
- React 项目使用 Motion 库（formerly framer-motion）

### 4. 空间与布局（Spatial Composition）

**核心原则**: 打破常规，创造意外的视觉节奏

```css
/* ✅ 推荐：不对称布局 */
.hero {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 4rem;
  align-items: center;
}

/* ✅ 推荐：大胆的负空间 */
.spacious {
  padding: 12rem 8rem;
}

/* ✅ 推荐：重叠元素 */
.overlap {
  position: relative;
  z-index: 1;
  margin-bottom: -3rem;
}
```

**布局突破**:
- 不对称网格
- 元素重叠
- 斜向流动
- 网格破坏元素
- 大胆的负空间 OR 控制的密度

### 5. 背景与视觉细节（Backgrounds & Visual Details）

**核心原则**: 创造氛围和深度，而非默认纯色

```css
/* ✅ 推荐：纹理和深度 */
.gradient-mesh {
  background: 
    radial-gradient(at 40% 20%, hsla(228, 100%, 50%, 0.15) 0px, transparent 50%),
    radial-gradient(at 80% 0%, hsla(189, 100%, 56%, 0.15) 0px, transparent 50%),
    radial-gradient(at 0% 50%, hsla(355, 100%, 93%, 0.2) 0px, transparent 50%);
}

/* ✅ 推荐：噪点纹理 */
.noise-overlay {
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,..."); /* SVG 噪点 */
  opacity: 0.03;
  pointer-events: none;
}

/* ✅ 推荐：戏剧性阴影 */
.card {
  box-shadow: 
    0 25px 50px -12px rgba(0, 0, 0, 0.25),
    0 0 0 1px rgba(0, 0, 0, 0.05);
}
```

**创意细节**:
- 渐变网格
- 噪点纹理
- 几何图案
- 层叠透明
- 戏剧性阴影
- 装饰性边框
- 自定义光标
- 颗粒叠加

---

## 实现指南

然后实现可工作的代码（HTML/CSS/JS、React、Vue 等），确保：

- **生产级且功能性**：代码可运行、符合最佳实践
- **视觉冲击且令人难忘**：有独特的美学观点
- **凝聚力强**：每个细节都服务于整体愿景
- **精心打磨**：间距、对比、动画都经过仔细推敲

### 实现复杂度匹配

**IMPORTANT**: 设计与实现复杂度要匹配。

- **极繁设计**：需要精心设计的代码，包含大量动画和效果
- **极简设计**：需要克制、精确、仔细关注间距、排版和微妙细节
- **优雅来自执行**：好的设计在于精确执行，而非添加更多元素

---

## 常见设计模式参考

### 科技感界面

```css
/* 深色背景 + 青色点缀 */
--bg: #0a0a0a;
--surface: #141414;
--border: #262626;
--accent: #22d3ee;
--text: #fafafa;
```

### 温暖自然界面

```css
/* 暖白背景 + 大地色点缀 */
--bg: #faf8f5;
--surface: #f5f1eb;
--border: #e8e2d9;
--accent: #e07a5f;
--text: #2d2a26;
```

### 极简高端界面

```css
/* 纯黑 + 高对比点缀 */
--bg: #ffffff;
--surface: #fafafa;
--border: #000000;
--accent: #000000;
--text: #000000;
```

---

## 禁止清单

NEVER 使用通用的 AI 生成美学：
- ❌ 过度使用的字体系列（Inter、Roboto、Arial、system fonts）
- ❌ 陈腐的配色方案（特别是白背景上的紫色渐变）
- ❌ 可预测的布局和组件模式
- ❌ 缺乏上下文特定性格的千篇一律设计
- ❌ Space Grotesk 等常见选择（跨代保持多样性）

---

## 质量检查清单

在完成设计前，检查以下各项：

- [ ] **字体选择**：是否独特且有意义？
- [ ] **色彩系统**：是否有明确的调色板？
- [ ] **动效设计**：是否有意图且有焦点？
- [ ] **空间布局**：是否打破常规？
- [ ] **视觉细节**：是否有深度和氛围？
- [ ] **无障碍**：是否符合 WCAG 标准？
- [ ] **响应式**：是否优雅适配各种屏幕？

---

**记住**: Claude 有能力创造非凡的创意作品。不要保守，展示当跳出框框思考并完全投入独特愿景时真正能创造的东西。
