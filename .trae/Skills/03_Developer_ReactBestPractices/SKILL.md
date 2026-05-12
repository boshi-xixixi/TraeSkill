---
name: vercel-react-best-practices
description: 当用户需要编写、审查或重构 React/Next.js 代码时使用。此 Skill 提供来自 Vercel Engineering 的 React 和 Next.js 性能优化指南，包含 45 条规则，涵盖组件优化、bundle 大小、数据获取等方面。
---

> **⚠️ 性能提示**: 此 Skill 包含 45 个 rules 文件（L1 ~50KB），专注于 React 性能优化。请根据实际场景选择性应用规则，优先处理 CRITICAL 和 HIGH 优先级的规则。

---

# Vercel React Best Practices

Comprehensive performance optimization guide for React and Next.js applications, maintained by Vercel. Contains 45 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

---

## 动画性能规范（Animation Performance）

在 React 应用中实现高性能动画，遵循 **compositor-only** 原则。

### 核心原则

浏览器可以在 compositor thread 上独立于主线程处理两种属性：
- ✅ `transform`
- ✅ `opacity`

所有其他属性（width, height, top, left, background 等）必须在主线程上计算，可能导致卡顿。

### 只允许的属性

```css
/* ✅ 允许：transform */
transform: translateX(100px);
transform: scale(1.1);
transform: rotate(45deg);
transform: skewX(10deg);

/* ✅ 允许：opacity */
opacity: 0;
opacity: 1;
```

### 禁止的属性

```css
/* ❌ 禁止：布局属性 */
width: 100%;
height: 200px;
top: 0;
left: 0;
margin: 10px;
padding: 20px;

/* ❌ 禁止：可能触发布局的属性 */
background-color: red;
border: 1px solid black;
color: blue;
```

### 动画实现示例

```jsx
// ❌ 不合规：使用 height 动画
function ExpandingBox() {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <div
      style={{
        height: isExpanded ? '200px' : '50px',
        transition: 'height 0.3s ease'
      }}
    >
      内容
    </div>
  );
}

// ✅ 合规：使用 transform 和 max-height
function ExpandingBox() {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <div
      style={{
        maxHeight: isExpanded ? '200px' : '50px',
        overflow: 'hidden',
        transition: 'max-height 0.3s ease'
      }}
    >
      内容
    </div>
  );
}

// ✅ 最佳：纯 transform
function ExpandingBox() {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <button onClick={() => setIsExpanded(!isExpanded)}>
      <span style={{
        transform: isExpanded ? 'rotate(180deg)' : 'rotate(0)',
        transition: 'transform 0.3s ease'
      }}>
        ▼
      </span>
      内容
    </button>
  );
}
```

### React 动画库使用规范

#### Framer Motion / Motion

```jsx
// ✅ 合规：使用 motion.div
import { motion } from 'framer-motion';

function AnimatedComponent() {
  return (
    <motion.div
      initial={{ opacity: 0, x: -100 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 0.5, ease: 'easeOut' }}
    >
      内容
    </motion.div>
  );
}

// ✅ 合规：使用 useTransform 限制属性
import { motion, useTransform } from 'framer-motion';

function ParallaxHeader() {
  const scrollY = useScroll();
  const y = useTransform(scrollY, [0, 500], [0, -200]);

  return (
    <motion.header style={{ y }}>
      内容
    </motion.header>
  );
}
```

#### Tailwind CSS 动画

```jsx
// ✅ 合规：使用 transform
<div className="transform hover:scale-105 transition-transform duration-200">
  内容
</div>

// ❌ 不合规：使用 width/height
<div className="w-0 hover:w-full transition-all duration-300">
  内容
</div>
```

### 性能检查清单

#### 必须遵守

- [ ] 只使用 `transform` 和 `opacity` 进行动画
- [ ] 所有动画元素有 `will-change` 提示
- [ ] 动画持续时间 ≤ 300ms（交互反馈）
- [ ] 使用 `transform: translate3d()` 启用 GPU 加速

#### 必须实现

- [ ] 支持 `prefers-reduced-motion`
- [ ] 离开视口时暂停动画
- [ ] 动画不阻塞主线程

```css
/* will-change 提示 */
.animated-element {
  will-change: transform, opacity;
}

/* prefers-reduced-motion 支持 */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

```jsx
// 暂停视口外动画
import { useInView } from 'framer-motion';

function LazyAnimation() {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-100px' });

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0 }}
      animate={isInView ? { opacity: 1 } : { opacity: 0 }}
    >
      内容
    </motion.div>
  );
}
```

### 常见错误示例

```jsx
// ❌ 错误 1：宽度动画
function Modal() {
  return (
    <div style={{
      width: isOpen ? '100%' : '0',
      transition: 'width 0.3s'
    }} />
  );
}

// ✅ 正确：使用 transform
function Modal() {
  return (
    <div style={{
      transform: isOpen ? 'scaleX(1)' : 'scaleX(0)',
      transformOrigin: 'left'
    }} />
  );
}

// ❌ 错误 2：颜色动画
function Button() {
  return (
    <button style={{
      backgroundColor: isHovered ? '#ff0000' : '#0000ff',
      transition: 'background-color 0.3s'
    }} />
  );
}

// ✅ 正确：使用 opacity 或绝对定位覆盖
function Button() {
  return (
    <button className="relative">
      <span className="bg-blue-500" />
      <span
        className="absolute inset-0 bg-red-500 opacity-0 hover:opacity-100 transition-opacity"
      />
    </button>
  );
}

// ❌ 错误 3：位置动画
function Draggable() {
  return (
    <div style={{
      top: y,
      left: x,
      transition: 'top 0.2s, left 0.2s'
    }} />
  );
}

// ✅ 正确：使用 transform
function Draggable() {
  return (
    <motion.div
      drag
      style={{ x, y }}
    />
  );
}
```

---

## When to Apply

Reference these guidelines when:
- Writing new React components or Next.js pages
- Implementing data fetching (client or server-side)
- Reviewing code for performance issues
- Refactoring existing React/Next.js code
- Optimizing bundle size or load times
- Implementing animations or transitions

---

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Eliminating Waterfalls | CRITICAL | `async-` |
| 2 | Bundle Size Optimization | CRITICAL | `bundle-` |
| 3 | Server-Side Performance | HIGH | `server-` |
| 4 | Client-Side Data Fetching | MEDIUM-HIGH | `client-` |
| 5 | Re-render Optimization | MEDIUM | `rerender-` |
| 6 | Rendering Performance | MEDIUM | `rendering-` |
| 7 | JavaScript Performance | LOW-MEDIUM | `js-` |
| 8 | Advanced Patterns | LOW | `advanced-` |

---

## Quick Reference

### 1. Eliminating Waterfalls (CRITICAL)

- `async-defer-await` - Move await into branches where actually used
- `async-parallel` - Use Promise.all() for independent operations
- `async-dependencies` - Use better-all for partial dependencies
- `async-api-routes` - Start promises early, await late in API routes
- `async-suspense-boundaries` - Use Suspense to stream content

### 2. Bundle Size Optimization (CRITICAL)

- `bundle-barrel-imports` - Import directly, avoid barrel files
- `bundle-dynamic-imports` - Use next/dynamic for heavy components
- `bundle-defer-third-party` - Load analytics/logging after hydration
- `bundle-conditional` - Load modules only when feature is activated
- `bundle-preload` - Preload on hover/focus for perceived speed

### 3. Server-Side Performance (HIGH)

- `server-cache-react` - Use React.cache() for per-request deduplication
- `server-cache-lru` - Use LRU cache for cross-request caching
- `server-serialization` - Minimize data passed to client components
- `server-parallel-fetching` - Restructure components to parallelize fetches
- `server-after-nonblocking` - Use after() for non-blocking operations

### 4. Client-Side Data Fetching (MEDIUM-HIGH)

- `client-swr-dedup` - Use SWR for automatic request deduplication
- `client-event-listeners` - Deduplicate global event listeners

### 5. Re-render Optimization (MEDIUM)

- `rerender-defer-reads` - Don't subscribe to state only used in callbacks
- `rerender-memo` - Extract expensive work into memoized components
- `rerender-dependencies` - Use primitive dependencies in effects
- `rerender-derived-state` - Subscribe to derived booleans, not raw values
- `rerender-functional-setstate` - Use functional setState for stable callbacks
- `rerender-lazy-state-init` - Pass function to useState for expensive values
- `rerender-transitions` - Use startTransition for non-urgent updates

### 6. Rendering Performance (MEDIUM)

- `rendering-animate-svg-wrapper` - Animate div wrapper, not SVG element
- `rendering-content-visibility` - Use content-visibility for long lists
- `rendering-hoist-jsx` - Extract static JSX outside components
- `rendering-svg-precision` - Reduce SVG coordinate precision
- `rendering-hydration-no-flicker` - Use inline script for client-only data
- `rendering-activity` - Use Activity component for show/hide
- `rendering-conditional-render` - Use ternary, not && for conditionals

### 7. JavaScript Performance (LOW-MEDIUM)

- `js-batch-dom-css` - Group CSS changes via classes or cssText
- `js-index-maps` - Build Map for repeated lookups
- `js-cache-property-access` - Cache object properties in loops
- `js-cache-function-results` - Cache function results in module-level Map
- `js-cache-storage` - Cache localStorage/sessionStorage reads
- `js-combine-iterations` - Combine multiple filter/map into one loop
- `js-length-check-first` - Check array length before expensive comparison
- `js-early-exit` - Return early from functions
- `js-hoist-regexp` - Hoist RegExp creation outside loops
- `js-min-max-loop` - Use loop for min/max instead of sort
- `js-set-map-lookups` - Use Set/Map for O(1) lookups
- `js-tosorted-immutable` - Use toSorted() for immutability

### 8. Advanced Patterns (LOW)

- `advanced-event-handler-refs` - Store event handlers in refs
- `advanced-use-latest` - useLatest for stable callback refs

---

## How to Use

Read individual rule files for detailed explanations and code examples:

```
rules/async-parallel.md
rules/bundle-barrel-imports.md
rules/_sections.md
```

Each rule file contains:
- Brief explanation of why it matters
- Incorrect code example with explanation
- Correct code example with explanation
- Additional context and references

---

## Full Compiled Document

For the complete guide with all rules expanded: `AGENTS.md`
