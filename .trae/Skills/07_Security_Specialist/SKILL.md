---
name: Security Specialist
description: 应用安全专家，专注于认证授权、数据保护和合规性审计。当用户需要：(1) 设计安全的登录认证系统 (2) 进行安全代码审查 (3) 检查 GDPR/隐私合规 (4) 防范常见安全漏洞 (OWASP Top 10) (5) 确保无障碍设计安全使用时使用此 Skill。
---

> **⚠️ 性能提示**: 此 Skill 包含完整的安全审计流程和无障碍安全指南。日常开发可只关注 OWASP Top 10 和快速安全检查清单。

---

# Security Specialist Skills

## 🤖 智能体与 MCP 增强 (Agent & MCP Enhancements)

本 Skill 支持并推荐配合特定的智能体角色和 MCP 工具使用，以获得最佳效果。

### 推荐智能体角色
*   **Security Auditor**: 详见 [AGENTS.md](AGENTS.md)。
    *   该角色具备"零信任"和"攻击者视角"，能够主动发现潜在风险。
    *   启用后，AI 将强制执行 OWASP 安全检查清单。

### 推荐 MCP 工具
*   **Git MCP**: 用于扫描历史提交中的敏感信息泄露。
*   **Filesystem MCP**: 用于检查文件权限和 `.gitignore` 配置。

---

提供全方位的安全保障，确保应用符合安全标准与法规。

---

## 包含的技能模块

### 1. [安全需求提取 (Security Requirements)](./安全需求提取.md)
- **核心价值**: 在设计阶段识别安全风险。
- **关键技术**: 威胁建模, STRIDE 分析, 安全用户故事.
- **使用场景**: 新功能安全评审、架构设计。

### 2. [认证实现模式 (Authentication)](./认证实现模式.md)
- **核心价值**: 实现安全可靠的用户身份验证。
- **关键技术**: JWT, OAuth2, OIDC, Session 管理.
- **使用场景**: 登录注册系统开发、第三方登录集成。

### 3. [GDPR 数据处理 (GDPR Compliance)](./GDPR数据处理.md)
- **核心价值**: 确保数据处理符合 GDPR 等隐私法规。
- **关键技术**: 数据最小化, 被遗忘权实现, 数据加密.
- **使用场景**: 出海应用开发、隐私合规审计。

### 4. 无障碍安全设计 (Accessibility Security)
- **核心价值**: 确保残障用户的安全使用体验。
- **关键技术**: 安全焦点管理, ARIA 安全使用, 验证码无障碍设计.
- **使用场景**: 无障碍网站安全审计、屏幕阅读器安全。

---

## 如何使用

- **登录设计**: "请参考认证实现模式，帮我设计一个安全的 JWT 登录流程。"
- **合规检查**: "请检查我的数据库字段设计是否符合 GDPR 要求。"
- **无障碍安全**: "请检查我的登录表单是否对屏幕阅读器用户安全且可访问。"

---

## 无障碍安全设计 (Accessibility Security)

### 为什么无障碍与安全相关？

无障碍设计不仅仅是可用性要求，也涉及安全层面：

| 安全问题 | 无障碍风险 | 安全影响 |
|---------|-----------|---------|
| 验证码绕过 | 视觉验证码无法被屏幕阅读器访问 | 可能迫使视障用户使用不安全的替代方案 |
| 焦点管理 | 模态框焦点泄漏 | 敏感信息可能被意外暴露 |
| ARIA 滥用 | aria-hidden 滥用 | 隐藏敏感内容被屏幕阅读器读取 |
| 输入验证 | 错误提示不清晰 | 用户可能重复提交导致安全问题 |

---

### 1. 验证码无障碍设计

#### 问题

传统验证码（CAPTCHA）对视障用户构成严重障碍：
- 视觉谜题无法被屏幕阅读器识别
- 音频验证码可能泄露信息
- 复杂的验证码增加认知负担

#### 解决方案

```html
<!-- ❌ 不合规：纯视觉验证码 -->
<div class="captcha">
  <img src="/captcha.png" alt="验证码图片" />
  <input type="text" placeholder="请输入验证码" />
</div>

<!-- ✅ 合规：提供多种验证方式 -->
<div class="captcha" role="group" aria-labelledby="captcha-label">
  <span id="captcha-label" class="sr-only">安全验证</span>

  <!-- 首选：隐形验证码 -->
  <div data-captcha="invisible"></div>

  <!-- 备选：音频验证码 -->
  <button type="button" aria-describedby="audio-desc">
    播放音频验证码
    <span id="audio-desc" class="sr-only">
      如有视觉障碍，请点击此处获取音频验证码
    </span>
  </button>

  <label for="captcha-input" class="sr-only">请输入您听到的字符</label>
  <input type="text" id="captcha-input" autocomplete="off" />
</div>
```

#### 最佳实践

1. **优先隐形验证码**：使用行为分析（如 reCAPTCHA v3）代替视觉挑战
2. **提供替代方案**：始终提供非视觉验证选项
3. **清晰的说明**：为所有验证码提供清晰的文字说明
4. **错误处理**：验证码错误时提供清晰的语音提示

```javascript
// ✅ 推荐：隐形验证码检查
async function validateCaptcha(token) {
  try {
    const response = await fetch('/api/verify-captcha', {
      method: 'POST',
      body: JSON.stringify({ token })
    });
    const result = await response.json();

    if (!result.success) {
      // 对屏幕阅读器用户显示语音错误
      announceToScreenReader('验证码验证失败，请重试');
      return false;
    }
    return true;
  } catch (error) {
    announceToScreenReader('网络错误，请稍后重试');
    return false;
  }
}
```

---

### 2. 安全焦点管理

#### 问题

焦点管理不当可能导致敏感信息泄露：
- 模态框外的敏感内容仍可被 Tab 访问
- 焦点泄漏到隐藏内容
- 焦点丢失在复杂页面中

#### 解决方案

```html
<!-- ❌ 不安全：模态框焦点泄漏 -->
<div class="modal">
  <h2>登录表单</h2>
  <input type="text" placeholder="用户名" />
  <input type="password" placeholder="密码" />
  <!-- 危险：背景内容仍可被访问 -->
</div>
<div class="background-content">
  <button>删除账户</button> <!-- 可被意外聚焦 -->
</div>

<!-- ✅ 安全：正确的焦点陷阱 -->
<div
  class="modal"
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-title"
  tabindex="-1"
>
  <h2 id="modal-title">登录表单</h2>

  <label for="username">用户名</label>
  <input type="text" id="username" autocomplete="username" />

  <label for="password">密码</label>
  <input type="password" id="password" autocomplete="current-password" />

  <button type="button" aria-describedby="password-requirements">
    显示密码要求
  </button>

  <!-- aria-describedby 安全使用 -->
  <p id="password-requirements" class="sr-only">
    密码要求：至少8个字符，包含大小写字母和数字
  </p>
</div>
```

```javascript
// ✅ 安全的焦点陷阱实现
class FocusTrap {
  constructor(modalElement) {
    this.modal = modalElement;
    this.firstFocusable = null;
    this.lastFocusable = null;
    this.previousActiveElement = null;
  }

  activate() {
    // 保存之前的焦点元素
    this.previousActiveElement = document.activeElement;

    // 找到焦点元素
    const focusableElements = this.modal.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );

    this.firstFocusable = focusableElements[0];
    this.lastFocusable = focusableElements[focusableElements.length - 1];

    // 将焦点移到模态框第一个元素
    this.firstFocusable.focus();

    // 添加键盘监听
    this.handleKeyDown = this.handleKeyDown.bind(this);
    document.addEventListener('keydown', this.handleKeyDown);
  }

  handleKeyDown(event) {
    if (event.key !== 'Tab') return;

    // Shift + Tab: 从第一个元素向前
    if (event.shiftKey && document.activeElement === this.firstFocusable) {
      event.preventDefault();
      this.lastFocusable.focus();
    }
    // Tab: 从最后一个元素向后
    else if (!event.shiftKey && document.activeElement === this.lastFocusable) {
      event.preventDefault();
      this.firstFocusable.focus();
    }
  }

  deactivate() {
    document.removeEventListener('keydown', this.handleKeyDown);
    // 恢复焦点
    if (this.previousActiveElement) {
      this.previousActiveElement.focus();
    }
  }
}
```

---

### 3. ARIA 安全使用

#### 问题

ARIA 属性使用不当可能导致安全信息泄露：
- `aria-hidden` 可能隐藏安全警告
- `aria-live` 可能意外暴露敏感信息
- `aria-describedby` 链接到错误的内容

#### 安全 ARIA 使用规范

```html
<!-- ❌ 不安全：隐藏安全警告 -->
<div aria-hidden="true" class="security-warning">
  ⚠️ 此页面包含敏感信息
</div>

<!-- ✅ 安全：保留重要安全信息 -->
<div
  role="alert"
  aria-live="assertive"
  class="security-warning"
>
  ⚠️ 此页面包含敏感信息，请确认您的网络连接安全
</div>
```

```html
<!-- ❌ 不安全：aria-describedby 链接到隐藏内容 -->
<span id="sensitive-info" class="sr-only">
  您的账户余额为 ¥10,000
</span>

<button aria-describedby="sensitive-info">
  查看详情
</button>

<!-- ✅ 安全：谨慎使用 aria-describedby -->
<button aria-describedby="button-purpose">
  查看详情
</button>
<span id="button-purpose" class="sr-only">
  查看账户详情和余额
</span>
```

#### ARIA 安全检查清单

- [ ] 不要使用 `aria-hidden` 隐藏重要安全信息
- [ ] `aria-live` 区域设置合理的优先级（assertive/polite）
- [ ] `aria-describedby` 只链接到相关内容
- [ ] 不要依赖 ARIA 隐藏敏感数据，使用真实 DOM 操作
- [ ] 屏幕阅读器用户应获得与视觉用户相同的安全提示

---

### 4. 表单安全与无障碍

#### 安全的输入验证

```html
<!-- ✅ 合规：安全的错误提示 -->
<label for="password">密码</label>
<input
  type="password"
  id="password"
  aria-describedby="password-requirements password-hint"
  aria-invalid="false"
/>
<ul id="password-requirements" class="sr-only">
  <li>至少8个字符</li>
  <li>包含大写字母</li>
  <li>包含小写字母</li>
  <li>包含数字</li>
</ul>

<!-- 安全提示，不暴露具体错误 -->
<p id="password-hint">
  请参考要求创建强密码
</p>

<div
  role="alert"
  aria-live="polite"
  id="password-error"
  hidden
>
</div>
```

```javascript
// ✅ 安全的错误提示
function validatePassword(password) {
  const errors = [];

  if (password.length < 8) {
    errors.push('密码长度不足');
  }
  if (!/[A-Z]/.test(password)) {
    errors.push('缺少大写字母');
  }

  const errorElement = document.getElementById('password-error');

  if (errors.length > 0) {
    // 设置 aria-invalid
    document.getElementById('password').setAttribute('aria-invalid', 'true');

    // 对屏幕阅读器显示通用错误
    errorElement.textContent = '密码不符合要求，请重试';
    errorElement.hidden = false;
  } else {
    document.getElementById('password').setAttribute('aria-invalid', 'false');
    errorElement.hidden = true;
  }
}
```

#### 安全的自动完成

```html
<!-- ✅ 合规：安全的自动完成 -->
<label for="cc-number">信用卡号</label>
<input
  type="text"
  id="cc-number"
  inputmode="numeric"
  pattern="[0-9\s]{13,19}"
  autocomplete="cc-number"
  aria-describedby="cc-hint"
/>
<p id="cc-hint" class="sr-only">
  输入13到19位数字，可包含空格
</p>

<!-- ❌ 危险：禁用自动完成可能导致用户使用不安全的密码 -->
<input type="password" autocomplete="off" />
```

---

### 5. 认证流程无障碍安全

#### 多因素认证（MFA）无障碍

```html
<!-- ✅ 合规：MFA 无障碍设计 -->
<section aria-labelledby="mfa-title">
  <h2 id="mfa-title">双因素认证</h2>

  <p>为了保护您的账户安全，我们建议启用双因素认证。</p>

  <!-- TOTP 应用 -->
  <div>
    <h3>身份验证器应用</h3>
    <button type="button">
      <svg aria-hidden="true"><!-- 图标 --></svg>
      <span>下载 Google Authenticator</span>
    </button>

    <label for="totp-code">输入6位验证码</label>
    <input
      type="text"
      id="totp-code"
      inputmode="numeric"
      pattern="[0-9]{6}"
      maxlength="6"
      autocomplete="one-time-code"
      aria-describedby="totp-hint"
    />
    <p id="totp-hint" class="sr-only">
      请输入身份验证器应用显示的6位数字验证码
    </p>
  </div>

  <!-- 短信验证码 -->
  <div>
    <h3>短信验证码</h3>
    <button type="button" aria-describedby="sms-warning">
      发送短信验证码
    </button>
    <p id="sms-warning" class="sr-only">
      注意：短信验证码可能存在安全风险，建议使用身份验证器应用
    </p>
  </div>
</section>
```

#### 安全的会话超时

```html
<!-- ✅ 合规：会话超时无障碍通知 -->
<div
  role="alertdialog"
  aria-labelledby="timeout-title"
  aria-describedby="timeout-desc"
  aria-modal="true"
>
  <h2 id="timeout-title">会话即将过期</h2>

  <p id="timeout-desc">
    由于您超过30分钟未操作，会话即将自动登出。
    <span id="countdown" aria-live="polite" aria-atomic="true">
      剩余 2 分钟
    </span>
  </p>

  <button type="button" onclick="extendSession()">
    继续操作
  </button>
  <button type="button" onclick="logout()">
    安全登出
  </button>
</div>
```

---

### 6. 无障碍安全测试

#### 自动化测试

```javascript
// jest-accessibility-security.test.js

describe('无障碍安全测试', () => {
  test('敏感信息不被 aria-hidden 隐藏', () => {
    const warnings = document.querySelectorAll('[aria-hidden="true"]');

    warnings.forEach(element => {
      const text = element.textContent.toLowerCase();
      const isSecurityRelated = text.includes('安全') ||
                                 text.includes('warning') ||
                                 text.includes('敏感');

      expect(isSecurityRelated).toBe(false);
    });
  });

  test('所有表单有安全的错误提示', () => {
    const inputs = document.querySelectorAll('input[aria-invalid="true"]');
    const errors = document.querySelectorAll('[role="alert"], [aria-live]');

    // 每个错误输入应该有对应的错误提示
    inputs.forEach(input => {
      const describedBy = input.getAttribute('aria-describedby');
      const hasErrorConnection = errors.some(error =>
        describedBy?.includes(error.id)
      );

      expect(hasErrorConnection).toBe(true);
    });
  });

  test('模态框有正确的焦点陷阱', () => {
    const modals = document.querySelectorAll('[role="dialog"]');

    modals.forEach(modal => {
      const focusableElements = modal.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      );

      // 模态框应该有可聚焦元素
      expect(focusableElements.length).toBeGreaterThan(0);

      // 第一个元素应该是可聚焦的
      expect(focusableElements[0]).toBeFocusable();
    });
  });
});
```

#### 手动测试检查清单

- [ ] 使用屏幕阅读器（NVDA/VoiceOver）测试所有安全提示是否可读
- [ ] 测试焦点管理：Tab 键是否只在模态框内循环
- [ ] 验证所有验证码选项对屏幕阅读器可用
- [ ] 检查所有错误提示是否使用 ARIA live 区域
- [ ] 测试键盘导航：是否所有安全操作都可键盘触发

---

### 7. 无障碍安全合规标准

#### WCAG 2.2 安全相关要求

| 标准 | 要求 | 无障碍安全实现 |
|------|------|---------------|
| 1.3.1 信息和关系 | 结构化信息 | 安全的表单结构和语义 |
| 2.1.1 键盘 | 完全键盘可访问 | 所有安全操作键盘可触发 |
| 2.4.3 焦点顺序 | 焦点顺序符合逻辑 | 安全的焦点管理 |
| 3.3.1 错误识别 | 错误识别 | 屏幕阅读器可感知的错误 |
| 4.1.2 名称角色值 | ARIA 正确使用 | 安全使用 ARIA 属性 |

#### OWASP 无障碍安全

- **身份验证**: 确保验证码对所有用户可用
- **会话管理**: 无障碍的会话超时提示
- **访问控制**: 焦点管理防止未授权访问
- **安全日志**: 屏幕阅读器可访问的安全事件

---

## 快速安全检查清单

### 日常开发

- [ ] 所有表单输入有正确的 label
- [ ] 错误提示使用 aria-describedby 或 aria-live
- [ ] 模态框有正确的焦点陷阱
- [ ] 没有用 aria-hidden 隐藏重要信息
- [ ] 验证码有非视觉替代方案

### 安全审计

- [ ] 检查所有 ARIA 使用是否安全
- [ ] 验证焦点管理不泄漏敏感信息
- [ ] 测试屏幕阅读器用户的安全流程
- [ ] 检查表单自动完成安全性

### 无障碍安全

- [ ] 验证屏幕阅读器可读取所有安全警告
- [ ] 测试键盘用户不会意外访问敏感内容
- [ ] 确保验证码对残障用户可用
- [ ] 检查错误消息不泄露安全细节

---

## 相关 Skill

- **WebGuidelines**: 无障碍设计和 WCAG 合规检查
- **FrontendImplementation**: 无障碍前端实现
- **ReactBestPractices**: React 组件的无障碍模式
- **DesignSystem**: 无障碍 Design Token

---

## 参考资料

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [WCAG 2.2 官方文档](https://www.w3.org/TR/WCAG22/)
- [WAI-ARIA 最佳实践](https://www.w3.org/WAI/ARIA/apg/)
- [WebAIM 无障碍和安全](https://webaim.org/techniques/security/)
