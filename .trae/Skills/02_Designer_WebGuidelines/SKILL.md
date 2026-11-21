---
name: web-design-guidelines
description: 当用户需要审查 UI 代码、进行可访问性检查、设计审计、优化页面性能或对照最佳实践检查网站时使用。此 Skill 对照 Web Interface Guidelines 和 WCAG 2.2 标准检查合规性，并用「先量再改 + 棘轮」的方法做性能优化。 触发词：UI 审计、可访问性检查、对比度不够、检查一下这个页面、页面太慢、首屏加载慢、优化性能。
argument-hint: <file-or-pattern>
---
> **⚠️ 性能提示**: 此 Skill 包含完整的 WCAG 2.2 检查清单。对于快速审查，可以只使用"快速检查清单"；对于完整审计，使用"详细检查清单"。

---

# Web Interface Guidelines & Accessibility Checker

## 概述

此 Skill 提供两种审查模式：

1. **快速审查**：基于 Vercel Web Interface Guidelines 的即时检查
2. **完整审计**：基于 WCAG 2.2 AA 标准的全面合规性检查

---

## 快速审查（Web Interface Guidelines）

### 工作流程

1. 从源 URL 获取最新指南：
   ```
   https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
   ```

2. 读取指定的文件（或提示用户提供文件/模式）

3. 对照获取的规则检查

4. 使用简洁的 `file:line` 格式输出结果

### 使用方式

当用户提供文件或模式参数时：
1. 从上述 URL 获取指南
2. 读取指定的文件
3. 应用所有规则
4. 按照指南中指定的格式输出结果

如果未指定文件，询问用户要审查哪些文件。

---

## 完整审计（WCAG 2.2 AA）

### WCAG 2.2 新增成功准则

WCAG 2.2 在 2.1 基础上增加了 9 个新成功准则：

#### 2.4.11 焦点外观（最小）（Focus Appearance (Minimum)）- AA

**要求**：焦点指示符必须满足以下所有条件：
- 对比度：至少 3:1（焦点与相邻颜色）
- 区域：指示符面积至少等于 1 CSS 像素环的面积
- 不被其他内容遮挡

**检查点**：
- [ ] 所有交互元素（链接、按钮、输入框）有可见焦点状态
- [ ] 焦点指示符对比度 ≥ 3:1
- [ ] 焦点样式不会被其他内容遮挡

```css
/* ✅ 合规的焦点样式 */
:focus {
  outline: 2px solid #005fcc;
  outline-offset: 2px;
}

/* ✅ 高对比度焦点 */
:focus {
  outline: 3px solid #000000;
  background: #ffff00;
}
```

#### 2.4.12 焦点不被隐藏（Focus Not Obscured）（最小）- AA

**要求**：焦点指示符不能被其他内容完全遮挡

**检查点**：
- [ ] 固定元素（header、nav）不会遮挡焦点
- [ ] 模态框打开时焦点元素可见
- [ ] 滚动时焦点元素保持在视口中

#### 2.5.7 拖动动作（Dragging Movements）- AA

**要求**：所有使用拖动操作的功能都应提供单指针替代方案

**检查点**：
- [ ] 滑块有 +/- 按钮替代拖动
- [ ] 拖放列表有上/下按钮替代拖动
- [ ] 拖动操作有清晰的视觉反馈

```jsx
// ❌ 不合规：只有拖动
<SortableList items={items} />

// ✅ 合规：提供替代方案
<SortableList items={items} />
<SortableList items={items} mode="buttons" />
```

#### 2.5.8 目标大小（最小）（Target Size (Minimum)）- AA

**要求**：触摸目标至少 24x24 CSS 像素

**检查点**：
- [ ] 按钮最小尺寸 24x24px
- [ ] 移动端触摸目标 ≥ 44x44px（WCAG 2.2 AAA）
- [ ] 目标之间有足够间距

```css
/* ✅ 合规的触摸目标 */
button {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 16px;
}
```

---

## 详细 WCAG 2.2 AA 检查清单

### 1. 可感知性（Perceivable）

#### 1.1.1 非文本内容 - 所有文本

- [ ] 所有图片有 alt 文本
- [ ] 复杂图像有长描述
- [ ] 图标按钮有 aria-label
- [ ] 表单有可见标签

```html
<!-- ✅ 合规 -->
<img src="chart.png" alt="2024年用户增长图表，显示同比增长25%" />

<!-- ❌ 不合规 -->
<img src="chart.png" />
```

#### 1.3.1 信息和关系

- [ ] 语义化 HTML 结构
- [ ] 标题层级正确（h1 → h2 → h3）
- [ ] 表单关联正确的 label
- [ ] 列表使用 ul/ol

```html
<!-- ✅ 合规 -->
<label for="email">邮箱地址</label>
<input type="email" id="email" name="email" />

<!-- ❌ 不合规 -->
<span>邮箱地址</span>
<input type="email" aria-label="邮箱" />
```

#### 1.4.3 对比度（最小）

**文本对比度要求**：
- 普通文本：4.5:1
- 大文本（18px+ 或 14px bold）：3:1
- UI 组件和图形对象：3:1

**检查工具**：
- Chrome DevTools > Lighthouse
- WebAIM Contrast Checker
-axe DevTools

```css
/* ✅ 合规 */
.text-primary {
  color: #1a1a1a; /* 对比度 16:1 on #ffffff */
}

.text-secondary {
  color: #5c5c5c; /* 对比度 7:1 on #ffffff */
}
```

#### 1.4.4 文本大小调整

- [ ] 文本可放大至 200% 而不丢失信息
- [ ] 使用相对单位（rem, em）而非固定单位（px）
- [ ] 避免 text-size-adjust 限制

```css
/* ✅ 合规 */
body {
  font-size: 1rem; /* = 16px default */
  line-height: 1.5;
}

h1 {
  font-size: 2rem; /* = 32px */
}
```

#### 1.4.11 非文本对比度

**UI 组件对比度要求**：
- 边框：3:1
- 焦点指示符：3:1
- 填充区域：3:1

```css
/* ✅ 合规 */
.input {
  border: 1px solid #767676; /* 对比度 4.5:1 */
  background: #ffffff;
}

.input:focus {
  border-color: #005fcc; /* 对比度 4.7:1 */
}
```

#### 1.4.12 文本间距

内容放大 200% 时不丢失信息：
- [ ] 字间距 ≥ 0.12em
- [ ] 词间距 ≥ 0.16em
- [ ] 行高 ≥ 1.5

```css
/* ✅ 合规 */
p {
  letter-spacing: 0.12em;
  word-spacing: 0.16em;
  line-height: 1.5;
}
```

#### 1.4.13 内容悬停（Content Hover on Hover）

- [ ] 可悬停内容可关闭
- [ ] 悬停可见，无需精确定位
- [ ] 悬停状态可被用户触发

---

### 2. 可操作性（Operable）

#### 2.1.1 键盘

**所有功能可通过键盘操作**：
- [ ] 所有交互元素可通过 Tab 访问
- [ ] 焦点顺序符合逻辑
- [ ] 自定义组件有键盘支持

**测试方法**：
1. 拔掉鼠标
2. 只用 Tab、Enter、Space、方向键操作
3. 确保所有功能可用

```jsx
// ✅ 合规的键盘支持
<div
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      handleClick();
    }
  }}
>
  点击我
</div>
```

#### 2.1.2 无键盘陷阱

- [ ] Tab 键可在所有区域自由移动
- [ ] Escape 键可关闭模态框/下拉菜单
- [ ] 没有意外的焦点循环

#### 2.4.1 跳过块

- [ ] 提供"跳转到主要内容"链接
- [ ] 跳过链接在焦点时可见

```html
<!-- ✅ 合规 -->
<a href="#main-content" class="skip-link">
  跳转到主要内容
</a>

<main id="main-content">
  <!-- 主要内容 -->
</main>

<style>
.skip-link {
  position: absolute;
  top: -100px;
}
.skip-link:focus {
  top: 0;
}
</style>
```

#### 2.4.3 焦点顺序

- [ ] 焦点顺序符合视觉和逻辑顺序
- [ ] DOM 顺序与视觉顺序一致
- [ ] 使用 tabindex 调整时注意顺序

#### 2.4.4 链接目的（语境）

- [ ] 链接文本描述目的
- [ ] 避免"点击这里"、"阅读更多"
- [ ] 同页面多个链接到同一目的地时文本相同

```html
<!-- ✅ 合规 -->
<a href="/pricing">查看定价方案</a>

<!-- ❌ 不合规 -->
<a href="/pricing">点击这里</a>
```

#### 2.4.6 标题和标签

- [ ] 标题描述主题或目的
- [ ] 标签描述输入目的
- [ ] 不要用占位符代替标签

```html
<!-- ✅ 合规 -->
<label for="search">搜索产品</label>
<input type="search" id="search" placeholder="输入关键词..." />

<!-- ❌ 不合规 -->
<input type="search" placeholder="搜索产品" />
```

#### 2.4.7 焦点可见

- [ ] 焦点指示符始终可见
- [ ] 不使用 `outline: none` 除非有替代方案

#### 2.5.3 标签名称（Label in Name）

- [ ] 可访问名称包含可视文本
- [ ] 图标按钮有可见标签

```html
<!-- ✅ 合规 -->
<button>
  <svg aria-hidden="true"><!-- ... --></svg>
  <span>提交</span>
</button>

<!-- ❌ 不合规 -->
<button aria-label="提交"></button>
```

#### 2.5.4 动作操纵（Motion Actuation）

- [ ] 功能不依赖特定手势
- [ ] 提供替代操作方式

---

### 3. 可理解性（Understandable）

#### 3.1.1 页面语言

- [ ] HTML 有 lang 属性
- [ ] lang 属性值正确

```html
<!-- ✅ 合规 -->
<html lang="zh-CN">
```

#### 3.2.1 焦点变化

- [ ] 焦点变化不自动触发上下文变化
- [ ] 用户主动触发而非自动转移

```html
<!-- ❌ 不合规 -->
<select onchange="this.form.submit()">

<!-- ✅ 合规 -->
<select onchange="confirm('确认选择？') && this.form.submit()">
```

#### 3.2.2 输入变化

- [ ] 输入变化不自动提交
- [ ] 用户主动触发提交

#### 3.3.1 错误识别

- [ ] 表单提交时识别错误
- [ ] 错误有文本描述
- [ ] 错误指向具体字段

```html
<!-- ✅ 合规 -->
<label for="email">邮箱</label>
<input type="email" id="email" aria-describedby="email-error" />
<span id="email-error" role="alert">
  请输入有效的邮箱地址
</span>

<!-- ❌ 不合规 -->
<input type="email" aria-invalid="true" />
```

#### 3.3.2 标签或说明

- [ ] 有输入说明时关联到输入
- [ ] 使用 aria-describedby

```html
<!-- ✅ 合规 -->
<label for="username">用户名</label>
<p id="username-hint">4-20个字符，可包含字母数字下划线</p>
<input id="username" aria-describedby="username-hint" />
```

---

### 4. 健壮性（Robust）

#### 4.1.1 解析

- [ ] HTML 有效且无重复 ID
- [ ] 使用验证工具检查

#### 4.1.2 名称、角色、值

- [ ] UI 组件有正确的名称、角色、值
- [ ] 使用原生 HTML 元素而非自定义 ARIA

```html
<!-- ✅ 合规 -->
<button>提交</button>

<!-- ❌ 不合规 -->
<div onclick="submit()">提交</div>
```

#### 4.1.3 状态消息

- [ ] 状态变化有文本通知
- [ ] 使用 aria-live 区域

```html
<!-- ✅ 合规 -->
<div aria-live="polite" aria-atomic="true">
  {statusMessage}
</div>
```

---

## 快速检查清单（日常使用）

### 必需项（必须通过）

- [ ] 所有图片有 alt 文本
- [ ] 所有表单输入有标签
- [ ] 颜色对比度 ≥ 4.5:1
- [ ] 键盘可访问所有功能
- [ ] 焦点指示符可见
- [ ] 链接文本描述目的

### 推荐项（强烈建议）

- [ ] 有跳过导航链接
- [ ] 标题层级正确
- [ ] 错误消息有描述
- [ ] 目标大小 ≥ 44px
- [ ] 支持 prefers-reduced-motion

---

## 测试工具推荐

### 自动化工具

- **axe DevTools**：浏览器扩展，实时检测可访问性问题
- **Lighthouse**：Chrome DevTools 内置，生成审计报告
- **WAVE**：WebAIM 开发，视觉化显示问题
- **Accessibility Insights**：微软开发，深度检测

### 手动测试

- **键盘测试**：拔掉鼠标，只用键盘操作
- **屏幕阅读器测试**：NVDA (Windows)、VoiceOver (macOS)
- **缩放测试**：放大至 200% 检查布局

---

## 修复优先级

### P0 - 立即修复

- 关键功能键盘不可用
- 主要内容无 alt 文本
- 对比度严重不足
- 表单错误无法识别

### P1 - 尽快修复

- 焦点指示符不明显
- 链接文本不明确
- 标题层级混乱
- 目标大小过小

### P2 - 计划修复

- 增强色盲支持
- 优化移动端体验
- 添加更多说明文本
- 优化动画体验

---

## 报告模板

```markdown
# 可访问性审计报告

## 概述
- **审计日期**: YYYY-MM-DD
- **审计范围**: [页面/组件/功能]
- **符合标准**: WCAG 2.2 AA

## 发现问题

### P0 - 立即修复
| 问题 | 位置 | 影响 | 建议修复 |
|------|------|------|---------|
| ... | ... | ... | ... |

### P1 - 尽快修复
| 问题 | 位置 | 影响 | 建议修复 |
|------|------|------|---------|
| ... | ... | ... | ... |

### P2 - 计划修复
| 问题 | 位置 | 影响 | 建议修复 |
|------|------|------|---------|
| ... | ... | ... | ... |

## 通过项目
- [ ] 列表
- [ ] 通过
- [ ] 的项目

## 建议
1. ...
2. ...
3. ...

## 参考资料
- [WCAG 2.2 官方文档](https://www.w3.org/TR/WCAG22/)
- [WebAIM 对比度检查](https://webaim.org/resources/contrastchecker/)
- [axe DevTools](https://www.deque.com/axe/)
```

---

## 性能优化：先量再改

**核心判断：能让 AI 量出来的东西，它才改得动。** 测量不是第零步（先埋点、等数据、再理解），而是第一步。

### 1. 定义"打开到能用"

不要用"页面加载完成"当终点。对每个核心操作定义一个可执行的判定：起点是导航开始或那次点击，终点是**真的能用**——能打字、能点主按钮、主要内容可见。

骨架屏、占位图、没有事件响应的空壳，都不算"能用"。把判定条件写成一段能在页面里跑的 JS 表达式，后面测速直接用。

### 2. 基线与拆解

- 实验室：同一脚本每组至少 10 次，报 p50 / p75 / p95，不要只报均值
- 线上：PageSpeed Insights 取 CrUX 真实用户 p75；没有数据就如实写没有
- 拆解：用 Resource Timing 把首屏时间拆开，标出哪些资源卡在关键路径上
- 计数：关键路径请求数、JS/CSS/图片字节数、主线程长任务总时长

### 3. 先建护栏，再动代码

改之前先把这几样跑绿，否则你无法判断是不是改坏了：

- 黄金测试：关键输出与基线逐字节一致
- 视觉回归：核心页面在两种宽度下截图，像素差在阈值内
- 功能冒烟：每个核心功能拿样例真跑一遍
- 内容站加 SEO：title、meta、canonical、结构化数据、链接逐项一致
- **基准上限（棘轮）**：把当前 p75 记为上限，之后只许降不许升

### 4. 找能数的代理指标，并证明它

真实耗时噪音大，适合当结论，不适合当每一步的闸门。用确定性指标（请求数、字节数、长任务时长、渲染次数）做判断，同样的代码跑多少次都是同一个数。

每个代理指标都要证明自己：至少两次改动里，它降了、真实耗时也跟着降。证明不了的就不用——否则是在爬一座错的山。

### 5. 爬山循环

每次改动都走同一条路：

1. 写假设：改什么、预计哪个计数会降、预计省多少毫秒
2. 做最小的那个改动
3. 跑护栏，有一项红就回退
4. 测速，没变快也回退
5. 记一条日志，一个改动一个 commit

### 6. 最终对比必须配对测

优化前后各起一个服务，在同一时段按 A、B、A、B 交替各测至少 10 次。分开时段测的数只能当过程记录，因为机器负载会变。

### 7. 三件事交给人

- **野心**：想停的时候，先问是不是太保守
- **品味**：用户能感知的变化（加载样子、动画时机），附前后截图让用户拍板
- **方向**：几百行只换来几毫秒的，主动提出不做

> 方法整理自 huashu-flash（MIT，https://github.com/alchaincyf/huashu-flash），源自 Anthropic《How we made claude.ai 3x faster in two weeks》的实践。

---

## 相关 Skill

- **FrontendImplementation**：设计时避免可访问性问题
- **ReactBestPractices**：React 组件的无障碍实现
- **Security Specialist**：包含安全相关的可访问性要求
