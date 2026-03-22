---
name: seo-technical-expert
description: "技术 SEO 专家，擅长网站性能优化、结构化数据、移动端优化和技术问题诊断。适用于网站技术实现、性能调优和搜索引擎抓取优化时使用。"
---

# Technical SEO Expert

## Overview

专注于网站技术层面的 SEO 优化，帮助一人企业确保网站在技术层面符合搜索引擎的要求，提升抓取效率、索引质量和用户体验。

## When to Use This Skill

- 网站技术问题诊断和修复
- 页面性能优化（Core Web Vitals）
- 结构化数据（Schema Markup）实施
- 移动端体验优化
- 抓取和索引问题排查
- 网站迁移和技术变更SEO审查
- HTTPS 和安全性配置
- URL 规范化和重定向管理

## Core Concepts

### 1. Core Web Vitals 优化

**核心指标标准（2024）：**

```
LCP (Largest Contentful Paint) - 最大内容绘制
├── 优秀：< 2.5 秒
├── 需要改进：2.5 - 4 秒
└── 差：> 4 秒
└── 优化方法：CDN、缓存、图片优化、代码分割

FID (First Input Delay) - 首次输入延迟（已替换为 INP）
INP (Interaction to Next Paint) - 交互到下次绘制
├── 优秀：< 200 毫秒
├── 需要改进：200 - 500 毫秒
└── 差：> 500 毫秒
└── 优化方法：减少 JavaScript 体积、事件处理优化、Web Worker

CLS (Cumulative Layout Shift) - 累积布局偏移
├── 优秀：< 0.1
├── 需要改进：0.1 - 0.25
└── 差：> 0.25
└── 优化方法：图片尺寸固定、字体加载优化、广告位预留
```

**性能优化工具：**
- Google PageSpeed Insights
- Lighthouse
- WebPageTest
- Chrome DevTools Performance 面板
- GTmetrix

### 2. 结构化数据 (Schema Markup)

**常用 Schema 类型：**

```json
// Article Schema（文章页）
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "文章标题",
  "author": {
    "@type": "Person",
    "name": "作者名"
  },
  "datePublished": "2024-01-15",
  "dateModified": "2024-01-15",
  "image": "图片URL",
  "publisher": {
    "@type": "Organization",
    "name": "网站名",
    "logo": {
      "@type": "ImageObject",
      "url": "Logo URL"
    }
  }
}

// Product Schema（产品页）
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "产品名称",
  "description": "产品描述",
  "image": "产品图片",
  "brand": {
    "@type": "Brand",
    "name": "品牌名"
  },
  "offers": {
    "@type": "Offer",
    "price": "99.00",
    "priceCurrency": "CNY",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "128"
  }
}

// FAQ Schema（常见问题页）
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "问题1",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "答案1"
      }
    },
    {
      "@type": "Question",
      "name": "问题2",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "答案2"
      }
    }
  ]
}

// LocalBusiness Schema（本地商家）
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "商家名称",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "街道地址",
    "addressLocality": "城市",
    "addressRegion": "省份",
    "postalCode": "邮编"
  },
  "telephone": "+86-xxx-xxxx-xxxx",
  "openingHours": "Mo-Fr 09:00-18:00",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "39.9042",
    "longitude": "116.4074"
  }
}
```

**Schema 实施检查清单：**
```markdown
- [ ] 使用 JSON-LD 格式（Google 推荐）
- [ ] 放置在 <head> 或 <body> 中
- [ ] 通过 Rich Results Test 验证
- [ ] 确认没有语法错误
- [ ] 对应页面类型匹配 Schema 类型
```

### 3. 移动端优化

**移动优先策略：**

```
响应式设计：
├── viewport meta 标签正确配置
├── 图片响应式 srcset
├── CSS 媒体查询适配
└── 触摸目标间距 >= 48px

移动性能：
├── 移动端 LCP < 2.5 秒
├── 首次渲染 < 1.8 秒
└── 交互延迟 < 100 毫秒

用户体验：
├── 字体大小 >= 16px（避免自动缩放）
├── 水平滚动条避免
└── 弹窗和插页式广告规范
```

**移动端友好性测试：**
- Google 移动端友好测试
- Chrome DevTools Device Mode
- BrowserStack 跨设备测试

### 4. 抓取和索引管理

** robots.txt 最佳实践：**

```
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /private/
Disallow: /checkout/
Disallow: /cart/

Sitemap: https://example.com/sitemap.xml

Crawl-delay: 1
```

** XML Sitemap 配置：**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/page/</loc>
    <lastmod>2024-01-15</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

**规范链接 (Canonical URL)：**

```html
<!-- 防止重复内容问题 -->
<link rel="canonical" href="https://example.com/canonical-page/" />

<!-- 处理参数和跟踪码 -->
<link rel="canonical" href="https://example.com/product/?utm_source=google" />
```

### 5. HTTPS 和安全

**安全检查清单：**
```markdown
- [ ] 全站 HTTPS
- [ ] SSL 证书有效且未过期
- [ ] HTTP 到 HTTPS 301 重定向
- [ ] HSTS 头配置
- [ ] 混合内容修复（HTTP 资源）
- [ ] 安全Headers配置（Content-Security-Policy 等）
```

### 6. 常见技术问题诊断

**问题：页面未被索引**

```
诊断步骤：
1. 检查 robots.txt 是否阻止抓取
2. 检查页面 canonical 是否指向其他URL
3. 使用 URL Inspection Tool 检查索引状态
4. 检查页面是否返回正确 HTTP 状态码
5. 审查页面内容和质量
```

**问题：抓取预算浪费**

```
优化建议：
1. 清理低价值页面（空页面、薄内容）
2. 设置参数处理规则（Google Search Console）
3. 优化内部链接结构
4. 使用 noindex 控制非必要页面索引
5. 提交 XML Sitemap 帮助蜘蛛发现新内容
```

**问题：重复内容**

```
解决方案：
1. 统一 URL 格式（带/不带 www）
2. 设置 canonical 标签
3. 处理 URL 参数问题
4. 使用 301 重定向合并相似页面
5. 创建独特有价值的内容
```

## Technical SEO 清单（一人企业快速部署）

### 第一周：基础配置

```
Day 1-2：技术审计
- 运行 Site Audit
- 识别关键问题（索引、速度、移动端）
- 制定修复优先级

Day 3-4：基础修复
- 配置 robots.txt
- 提交 XML Sitemap
- 设置 canonical URLs
- 启用 HTTPS

Day 5-7：性能基础
- 图像压缩和格式优化
- 启用浏览器缓存
- 配置 CDN（如使用）
```

### 第二周：进阶优化

```
Day 1-2：结构化数据
- 实现 Article/Product Schema
- 通过测试工具验证
- 监控 Rich Results 表现

Day 3-4：Core Web Vitals
- LCP 优化（图片、服务器响应）
- CLS 优化（布局稳定性）
- INP 优化（JavaScript 执行）

Day 5：监控设置
- Google Search Console
- Google Analytics 4
- 排名追踪工具配置
```

## Best Practices

1. **渐进式优化**：从小处着手，持续改进
2. **监控变化**：任何技术变更后监控索引状态
3. **文档记录**：记录所有技术变更和效果
4. **备份优先**：重大变更前确保可回滚
5. **测试环境**：重大变更前在测试环境验证

## Tools & Resources

### 免费工具
- Google Search Console
- Google PageSpeed Insights
- Lighthouse
- Schema Markup Validator
- Rich Results Test
- Mobile-Friendly Test
- Screaming Frog SEO Spider (免费版 500 URL)

### 付费工具
- Ahrefs Site Audit
- SEMrush
- Moz Pro
- Screaming Frog (高级版)
- GTmetrix Pro

## Common Pitfalls

- 忽略移动端用户体验
- 结构化数据错误实施
- 过度依赖 JavaScript 渲染
- 忽视 Core Web Vitals
- 错误的 robots.txt 配置
- 忽视 HTTPS 安全警告
