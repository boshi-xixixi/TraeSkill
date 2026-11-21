---
name: designer-motion
description: 当用户需要给界面加动效、做交互反馈、审查现有动画质量，或判断某个地方"该不该动"时使用。覆盖曲线与时长选择、进场/退场、列表交错、手势跟手、性能与 prefers-reduced-motion，输出可直接落地的 CSS / WAAPI / GSAP / Framer Motion 代码。触发词：加个动效、这个过渡好别扭、动画掉帧、入场动画、悬停效果、按钮点了没反馈。
argument-hint: <组件或页面路径>
---

# 动效设计与实现

动效不是装饰，是**解释界面发生了什么**。每加一个动画，先能回答"它在帮用户理解什么"，答不上来就不要加。

## 一、决策顺序

按这个顺序做决定，顺序错了后面怎么调都别扭：

1. **该不该动** —— 高频操作、键盘触发、数据刷新不要动
2. **动给谁看** —— 告知状态变化 / 引导注意力 / 表达空间关系 / 提供操作反馈
3. **用哪个工具** —— CSS / WAAPI / GSAP / Framer Motion
4. **动哪些属性** —— 只动 `transform` 和 `opacity`
5. **多快、什么曲线** —— 见下方档位表
6. **怎么被打断、怎么退出** —— 退出比进入快，且要能被中途接管

## 二、属性：只动合成层

| 属性 | 是否推荐 | 原因 |
|:---|:---|:---|
| `transform`、`opacity` | ✅ 首选 | 只走合成，不触发布局与重绘 |
| `filter`、`clip-path` | ⚠️ 谨慎 | 开销较高，长列表里慎用 |
| `width`/`height`/`top`/`left`/`margin` | ❌ 避免 | 每帧触发布局，必掉帧 |
| `box-shadow` | ⚠️ 谨慎 | 用伪元素 + opacity 代替 |
| `background-color` | ✅ 可用 | 只重绘，短时过渡可接受 |

`will-change` 只在动画开始前加、结束后移除，长期挂着会白白吃显存。

## 三、曲线与时长

**曲线**

- 进场（元素出现）：`ease-out`，起步快、收尾稳
- 退场（元素消失）：`ease-in`，起步慢、加速离开
- 位移和变形：不要用 `linear`，会显得机械
- 跟手/物理感：用弹簧，不要硬编码曲线
- 可用于接近 iOS 手感的缓动：`cubic-bezier(0.32, 0.72, 0, 1)`

**时长档位**

| 场景 | 时长 |
|:---|:---|
| hover / 按压反馈 | 100–150ms |
| 小元素出现（图标、徽标） | 150–250ms |
| 弹层、下拉、抽屉 | 200–300ms |
| 页面级转场 | 300–500ms |
| 叙事型滚动动画 | 可更长，但必须可跳过 |

超过 400ms 的过渡，用户会开始觉得"卡"而不是"顺"。

## 四、编排

- 一组元素入场：每个元素间隔 **30–80ms**，且延迟不要完全等距，等距会显得机械
- 一个容器只做**一次**入场，不要让每个子块各自 fade-in
- 明显的主次：主元素先动，辅助元素跟随或不动
- 同时动的元素超过 3 个，要考虑减少

## 五、工具选择

| 需求 | 选择 |
|:---|:---|
| 简单的状态过渡（hover、展开、淡入） | CSS `transition` |
| 需要循环或关键帧 | CSS `@keyframes` |
| 需要 JS 控制播放/暂停/进度 | Web Animations API `element.animate()` |
| 复杂时间线、滚动绑定、SVG 变形 | GSAP + ScrollTrigger |
| React 内的进出场、布局动画、手势 | Framer Motion / Motion |
| 跟手拖拽、弹簧物理 | 优先用库（如 Vaul、Motion），不要手搓 |

原则：CSS 能做的不要上库，库能解决的不手搓。

## 六、可访问性与性能

**必须处理 reduced motion**

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

GSAP 场景用 `gsap.matchMedia()` 包一层：

```js
const mm = gsap.matchMedia();
mm.add('(prefers-reduced-motion: no-preference)', () => {
  // 动画代码
});
```

**性能自查**

- 用 DevTools Performance 录制，确认动画期间没有 Layout / Recalculate Style
- 掉帧时先看是不是动了非合成属性，其次看主线程是否被 JS 长任务占住
- 滚动联动动画优先用 CSS `animation-timeline: scroll()` 或 `IntersectionObserver`，不要在 `scroll` 事件里同步改样式

## 七、手势交互

手势是直接操作，规则只有一条：**手指按下时，UI 必须等于手指**。

- 位移比例 1:1，不要做缓动跟随（那会"粘手"）
- 松手后由速度决定去向，不是固定阈值
- 动画必须能被中途抓住并反向
- 遮罩透明度、圆角、缩放，全部和拖拽进度线性绑定

## 八、常见错误清单

审查时逐条对照：

- [ ] 进场用了 `ease-in`，或者位移用了 `linear`
- [ ] 每个 section 都有 fade-in，滚动到底就"全部消失又出现"
- [ ] 列表项等距 stagger，且延迟 > 100ms
- [ ] 退出比进入还慢
- [ ] 动效期间无法交互（点了没反应）
- [ ] hover 有动效但触屏上粘住（sticky hover）
- [ ] 没写 `prefers-reduced-motion`
- [ ] 动画了 `height` / `top` / `margin`
- [ ] toast、tooltip 这种高频反馈带了 300ms 以上动画
- [ ] 键盘快捷键触发的操作带动画（应当瞬时）

## 九、输出约定

给出动效方案时，至少包含：

1. 触发条件与动画目的（一句话）
2. 属性 + 起止值
3. 时长 + 缓动曲线（具体数值，不要"适中""稍快"）
4. 打断与退出行为
5. reduced-motion 下的降级
6. 完整可复制代码

不确定某处要不要加动效时，先问："不加会怎样？"如果答案是"也没关系"，那就不加。
