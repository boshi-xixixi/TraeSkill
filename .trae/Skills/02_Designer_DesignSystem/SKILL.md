---
name: Design System Expert
description: 当用户需要管理品牌设计系统、创建 Design Token、定义组件规范或建立团队设计标准时使用。此 Skill 提供完整的设计系统构建方法，涵盖色彩系统、字体系统、组件库和样式指南。
---

> **⚠️ 性能提示**: 此 Skill 包含多个 Design Token 模板和组件规范示例。根据实际需求选择性使用，无需一次加载全部内容。

---

# Design System Expert

## 什么是 Design System？

Design System（设计系统）是一套可复用的设计规范和组件库，用于确保产品在不同平台和团队间的一致性。

### 核心组成部分

| 组成部分 | 说明 | 示例 |
|---------|------|------|
| **Design Token** | 设计原子，存储视觉属性 | 颜色、间距、字体 |
| **组件库** | 可复用 UI 组件 | Button、Input、Modal |
| **样式指南** | 设计规范文档 | 排版规范、间距系统 |
| **最佳实践** | 使用场景和代码示例 | 组件使用示例 |

---

## Design Token 设计

### 什么是 Design Token？

Design Token 是设计系统的原子单位，以键值对形式存储设计决策：

```json
{
  "color.primary": "#4F46E5",
  "spacing.4": "16px",
  "fontSize.base": "16px"
}
```

### 色彩 Token

```css
/* ❌ 避免：直接使用颜色值 */
.button {
  background-color: #4F46E5;
}

/* ✅ 推荐：使用 Token */
.button {
  background-color: var(--color-primary);
}
```

### Token 命名规范

#### 层级命名法

```
{属性}.{类别}.{变体}.{状态}

示例：
color.primary.500        /* 基础色 */
color.primary.hover       /* 悬停状态 */
color.primary.disabled    /* 禁用状态 */
color.text.primary        /* 主文本 */
color.text.secondary      /* 次要文本 */
color.background.surface  /* 表面背景 */
```

#### 语义命名法

```
{语义}.{用途}

示例：
color.brand.primary       /* 品牌主色 */
color.brand.secondary      /* 品牌次色 */
color.semantic.success     /* 成功语义色 */
color.semantic.error       /* 错误语义色 */
color.semantic.warning     /* 警告语义色 */
```

---

## 色彩系统

### 基础色彩扩展

每个基础色应该扩展为完整的色阶：

```css
:root {
  /* 蓝色色阶 */
  --blue-50: #eff6ff;
  --blue-100: #dbeafe;
  --blue-200: #bfdbfe;
  --blue-300: #93c5fd;
  --blue-400: #60a5fa;
  --blue-500: #3b82f6;
  --blue-600: #2563eb;
  --blue-700: #1d4ed8;
  --blue-800: #1e40af;
  --blue-900: #1e3a8a;
  --blue-950: #172554;
}
```

### 语义色彩

```css
:root {
  /* 品牌色 */
  --color-brand-primary: var(--blue-600);
  --color-brand-secondary: var(--indigo-600);

  /* 语义色 */
  --color-success: var(--green-600);
  --color-warning: var(--amber-500);
  --color-error: var(--red-600);
  --color-info: var(--blue-600);

  /* 中性色 */
  --color-neutral-50: #fafafa;
  --color-neutral-100: #f5f5f5;
  --color-neutral-200: #e5e5e5;
  --color-neutral-300: #d4d4d4;
  --color-neutral-400: #a3a3a3;
  --color-neutral-500: #737373;
  --color-neutral-600: #525252;
  --color-neutral-700: #404040;
  --color-neutral-800: #262626;
  --color-neutral-900: #171717;
  --color-neutral-950: #0a0a0a;
}
```

### 深色模式支持

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-background: var(--color-neutral-950);
    --color-surface: var(--color-neutral-900);
    --color-text-primary: var(--color-neutral-50);
    --color-text-secondary: var(--color-neutral-400);
    --color-border: var(--color-neutral-800);
  }
}

/* 或使用 .dark 主题类 */
.dark {
  --color-background: var(--color-neutral-950);
  --color-surface: var(--color-neutral-900);
  --color-text-primary: var(--color-neutral-50);
  --color-text-secondary: var(--color-neutral-400);
  --color-border: var(--color-neutral-800);
}
```

---

## 字体系统

### 字体 Token

```css
:root {
  /* 字体族 */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
  --font-serif: 'Playfair Display', Georgia, serif;

  /* 字体大小 */
  --text-xs: 0.75rem;    /* 12px */
  --text-sm: 0.875rem;   /* 14px */
  --text-base: 1rem;      /* 16px */
  --text-lg: 1.125rem;    /* 18px */
  --text-xl: 1.25rem;     /* 20px */
  --text-2xl: 1.5rem;     /* 24px */
  --text-3xl: 1.875rem;   /* 30px */
  --text-4xl: 2.25rem;    /* 36px */
  --text-5xl: 3rem;       /* 48px */

  /* 字体粗细 */
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;

  /* 行高 */
  --leading-none: 1;
  --leading-tight: 1.25;
  --leading-snug: 1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;

  /* 字间距 */
  --tracking-tighter: -0.05em;
  --tracking-tight: -0.025em;
  --tracking-normal: 0;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
}
```

### 排版规范

```css
/* 标题样式 */
.heading-1 {
  font-size: var(--text-5xl);
  font-weight: var(--font-bold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
}

.heading-2 {
  font-size: var(--text-4xl);
  font-weight: var(--font-semibold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
}

/* 正文样式 */
.body-large {
  font-size: var(--text-lg);
  font-weight: var(--font-normal);
  line-height: var(--leading-relaxed);
}

.body-base {
  font-size: var(--text-base);
  font-weight: var(--font-normal);
  line-height: var(--leading-normal);
}

.body-small {
  font-size: var(--text-sm);
  font-weight: var(--font-normal);
  line-height: var(--leading-normal);
}

/* 标签样式 */
.label {
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  line-height: var(--leading-none);
  letter-spacing: var(--tracking-wide);
  text-transform: uppercase;
}
```

---

## 间距系统

### 基础间距

```css
:root {
  /* 使用 4px 基准 */
  --space-0: 0;
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;     /* 8px */
  --space-3: 0.75rem;    /* 12px */
  --space-4: 1rem;       /* 16px */
  --space-5: 1.25rem;    /* 20px */
  --space-6: 1.5rem;     /* 24px */
  --space-8: 2rem;       /* 32px */
  --space-10: 2.5rem;    /* 40px */
  --space-12: 3rem;      /* 48px */
  --space-16: 4rem;      /* 64px */
  --space-20: 5rem;      /* 80px */
  --space-24: 6rem;      /* 96px */
}
```

### 语义间距

```css
:root {
  /* 组件内间距 */
  --spacing-inline-xs: var(--space-1);  /* 4px */
  --spacing-inline-sm: var(--space-2);  /* 8px */
  --spacing-inline-md: var(--space-3);  /* 12px */
  --spacing-inline-lg: var(--space-4);  /* 16px */

  /* 组件间间距 */
  --spacing-stack-xs: var(--space-2);   /* 8px */
  --spacing-stack-sm: var(--space-3);   /* 12px */
  --spacing-stack-md: var(--space-4);    /* 16px */
  --spacing-stack-lg: var(--space-6);    /* 24px */
  --spacing-stack-xl: var(--space-8);   /* 32px */

  /* 页面间距 */
  --spacing-page-sm: var(--space-4);    /* 16px */
  --spacing-page-md: var(--space-6);    /* 24px */
  --spacing-page-lg: var(--space-8);    /* 32px */
}
```

---

## 圆角系统

```css
:root {
  /* 基础圆角值 */
  --radius-none: 0;
  --radius-sm: 0.125rem;  /* 2px */
  --radius-md: 0.25rem;    /* 4px */
  --radius-lg: 0.5rem;      /* 8px */
  --radius-xl: 0.75rem;     /* 12px */
  --radius-2xl: 1rem;       /* 16px */
  --radius-full: 9999px;     /* 圆形/药丸形 */

  /* 语义圆角 */
  --radius-button: var(--radius-lg);
  --radius-input: var(--radius-md);
  --radius-card: var(--radius-xl);
  --radius-avatar: var(--radius-full);
  --radius-badge: var(--radius-full);
}
```

---

## 阴影系统

```css
:root {
  /* 基础阴影 */
  --shadow-xs: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-sm: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
  --shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.25);

  /* 语义阴影 */
  --shadow-card: var(--shadow-sm);
  --shadow-button: var(--shadow-xs);
  --shadow-modal: var(--shadow-xl);
  --shadow-dropdown: var(--shadow-lg);
}
```

---

## 组件规范

### Button 组件

```css
.button {
  /* 基础样式 */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-4);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  line-height: var(--leading-none);
  border-radius: var(--radius-button);
  cursor: pointer;
  transition: all 0.2s ease;

  /* 禁用状态 */
  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
}

/* 变体 */
.button--primary {
  background-color: var(--color-primary);
  color: white;

  &:hover:not(:disabled) {
    background-color: var(--color-primary-hover);
  }
}

.button--secondary {
  background-color: transparent;
  border: 1px solid var(--color-border);
  color: var(--color-text-primary);

  &:hover:not(:disabled) {
    background-color: var(--color-surface);
  }
}

.button--ghost {
  background-color: transparent;
  color: var(--color-text-primary);

  &:hover:not(:disabled) {
    background-color: var(--color-surface);
  }
}

/* 尺寸 */
.button--sm {
  padding: var(--space-1) var(--space-3);
  font-size: var(--text-xs);
}

.button--lg {
  padding: var(--space-3) var(--space-6);
  font-size: var(--text-base);
}
```

### Input 组件

```css
.input {
  /* 基础样式 */
  display: block;
  width: 100%;
  padding: var(--space-2) var(--space-3);
  font-size: var(--text-base);
  line-height: var(--leading-normal);
  color: var(--color-text-primary);
  background-color: var(--color-background);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-input);
  transition: border-color 0.2s ease, box-shadow 0.2s ease;

  /* 焦点状态 */
  &:focus {
    outline: none;
    border-color: var(--color-primary);
    box-shadow: 0 0 0 3px var(--color-primary-alpha-20);
  }

  /* 错误状态 */
  &.input--error {
    border-color: var(--color-error);

    &:focus {
      box-shadow: 0 0 0 3px var(--color-error-alpha-20);
    }
  }

  /* 禁用状态 */
  &:disabled {
    background-color: var(--color-surface);
    cursor: not-allowed;
  }
}
```

---

## 主题切换

### CSS 变量主题

```css
/* 默认主题 */
:root {
  --color-primary: #4F46E5;
  --color-background: #ffffff;
  --color-text: #1a1a1a;
}

/* 深色主题 */
[data-theme="dark"] {
  --color-primary: #6366f1;
  --color-background: #0a0a0a;
  --color-text: #fafafa;
}
```

### React 主题上下文

```jsx
// ThemeContext.tsx
import { createContext, useContext, useState } from 'react';

type Theme = 'light' | 'dark';

const ThemeContext = createContext<{
  theme: Theme;
  setTheme: (theme: Theme) => void;
}>({
  theme: 'light',
  setTheme: () => {},
});

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState<Theme>('light');

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <div data-theme={theme}>
        {children}
      </div>
    </ThemeContext.Provider>
  );
}

export const useTheme = () => useContext(ThemeContext);
```

---

## 设计系统文档

### 文档结构

```
design-system/
├── README.md
├── tokens/
│   ├── colors.json
│   ├── typography.json
│   ├── spacing.json
│   └── index.json
├── components/
│   ├── Button/
│   │   ├── Button.tsx
│   │   ├── Button.css
│   │   └── index.ts
│   ├── Input/
│   │   └── ...
├── guidelines/
│   ├── colors.md
│   ├── typography.md
│   └── spacing.md
└── examples/
    └── ...
```

### 文档模板

```markdown
# {组件名称}

## 概述
{组件的功能描述}

## 变体
- **Primary**: 主要操作
- **Secondary**: 次要操作
- **Ghost**: 幽灵按钮

## 尺寸
- **Small**: 小尺寸
- **Medium**: 中尺寸（默认）
- **Large**: 大尺寸

## 状态
- **Default**: 默认状态
- **Hover**: 悬停状态
- **Active**: 激活状态
- **Disabled**: 禁用状态
- **Loading**: 加载状态

## 使用示例

```tsx
<Button variant="primary" size="medium">
  按钮文字
</Button>
```

## 访问性
- 键盘可访问
- 支持屏幕阅读器
- 焦点状态可见
```

---

## 质量检查清单

### Design Token 检查

- [ ] 颜色 Token 有完整的色阶
- [ ] 语义命名清晰易懂
- [ ] Token 支持深色模式
- [ ] Token 导出为多种格式（CSS/SCSS/JSON）

### 组件规范检查

- [ ] 组件有完整的状态（默认、悬停、激活、禁用、加载）
- [ ] 组件有合理的尺寸变体
- [ ] 组件符合无障碍标准
- [ ] 组件有 TypeScript 类型定义

### 文档检查

- [ ] 每个组件有使用示例
- [ ] 文档包含代码片段
- [ ] 文档包含访问性说明
- [ ] 文档有版本历史记录

---

## 工具和资源

### Design Token 工具

- **Style Dictionary**: Amazon 开发的跨平台 Design Token 管理工具
- **Theo**: Airbnb 开发的 Design Token 转换工具
- **Design Tokens Plugin**: Figma 插件，直接从 Figma 导出 Token

### 组件库工具

- **Storybook**: 组件开发和文档工具
- **Chromatic**: Storybook 视觉测试平台
- **Bit**: 组件共享平台

### 样式指南工具

- **Zeroheight**: 设计系统文档平台
- **Notion**: 文档协作工具
- **Confluence**: 企业知识管理

---

## 相关 Skill

- **FrontendImplementation**: 设计系统应用的前端实现
- **UIUXIntelligence**: UI/UX 设计智能推荐
- **WebGuidelines**: 可访问性规范检查
