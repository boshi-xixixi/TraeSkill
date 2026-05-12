---
name: Backend Python Expert
description: 当用户需要进行 Python 后端开发时使用。此 Skill 提供 FastAPI 开发、异步编程和性能优化等 Python 后端开发全栈能力支持。
dependencies:
  - 05_Backend_Database
---

# Backend Python Skills

提供 Python 后端开发的全栈能力支持。

## 🤖 智能体与 MCP 增强 (Agent & MCP Enhancements)

本 Skill 支持并推荐配合特定的智能体角色和 MCP 工具使用，以获得最佳效果。

### 推荐智能体角色
*   **Python Backend Expert**: 详见 [AGENTS.md](AGENTS.md)。
    *   该角色专注于 FastAPI、异步编程和性能优化。
    *   启用后，AI 将优先使用 Pydantic 进行类型验证，关注异步性能。

### 推荐 MCP 工具
*   **PostgreSQL/MySQL MCP**: 直接执行 SQL 查询验证，获取实时 Schema 信息。
*   **mcp-feedback-enhanced**: 在设计 API 或数据库结构时，主动向用户确认业务需求。

---

## 包含的技能模块

### 1. [FastAPI 模板](./references/FastAPI模板.md)
- **核心价值**: 快速构建高性能的现代 Web API。
- **关键技术**: Pydantic 验证, 依赖注入, OpenAPI 文档。
- **使用场景**: 微服务开发、API 网关构建。

### 2. [Python 性能优化](./references/Python性能优化.md)
- **核心价值**: 提升 Python 代码的执行效率。
- **关键技术**: Profiling, 多进程/多线程, 算法优化。
- **使用场景**: 计算密集型任务、高并发服务。

### 3. [异步 Python 模式](./references/异步Python模式.md)
- **核心价值**: 掌握 asyncio，编写高效的非阻塞代码。
- **关键技术**: async/await, 协程管理, 异步 I/O。
- **使用场景**: I/O 密集型服务、实时通信。

### 4. [Python 测试模式](./references/Python测试模式.md)
- **核心价值**: 建立稳固的自动化测试体系。
- **关键技术**: Pytest, Mocking, Fixtures。
- **使用场景**: 单元测试、集成测试编写。

## 实用脚本

### 初始化 FastAPI 项目

```bash
# 创建新项目
python scripts/init_fastapi_project.py my_project --path ./projects

# 生成的目录结构:
# my_project/
# ├── app/
# │   ├── api/v1/endpoints/
# │   ├── core/config.py
# │   ├── models/
# │   ├── schemas/
# │   ├── services/
# │   └── main.py
# ├── tests/
# ├── requirements.txt
# └── pyproject.toml
```

## 如何使用

- **API 开发**: "请使用 FastAPI 模板帮我创建一个用户注册接口。"
- **并发优化**: "请参考异步 Python 模式，帮我优化这个爬虫脚本。"
- **项目初始化**: "帮我初始化一个 FastAPI 项目，项目名叫 user_service。"
