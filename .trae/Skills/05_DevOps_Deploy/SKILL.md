---
name: deploy-engineer
description: 当用户要把本地项目放到服务器上、配置域名与 HTTPS、写 Docker Compose 或排查"本地能跑线上报错"时使用。面向单机与轻量云服务器，不是 Kubernetes。触发词：部署上线、怎么让别人访问、域名配一下、服务器上跑不起来、配个 HTTPS、端口打不开、日志在哪看。
argument-hint: <项目路径或服务器地址>
---

# 单机部署与上线

目标：让一个项目在服务器上**稳定跑起来、能被访问、出问题能查**。不追求 Kubernetes 那套。

## 一、先选路线

| 项目类型 | 推荐方式 | 说明 |
|:---|:---|:---|
| 纯静态（HTML/CSS/JS） | Nginx 静态托管 | 最简单，别上 Node |
| Node / Python 常驻服务 | Docker Compose 或 PM2/systemd | 单机优先 Compose |
| 需要数据库 | Compose 带上 db + 卷 | 数据目录必须挂出来 |
| Serverless 友好（Next.js 等） | 平台托管 | 如果已有平台就别自建 |

**不要一上来就上 K8s**，单机 + Compose 足够撑到很大量级。

## 二、上线检查清单

按顺序核对，缺一项就可能卡住：

- [ ] 端口：应用监听 `0.0.0.0`，不是 `127.0.0.1`
- [ ] 防火墙：云厂商安全组 + 系统防火墙（ufw/firewalld）都放行
- [ ] 环境变量：`.env` 不进仓库，服务器上单独配
- [ ] 数据库：连接串指向 `127.0.0.1` 或容器名，不是 `localhost` 以外瞎写
- [ ] 构建产物：确认是 `build` 后的版本，不是 dev server
- [ ] 时区：容器默认 UTC，需要本地时间就设 `TZ=Asia/Shanghai`
- [ ] 日志：落到文件或 docker logs，别只打 stdout 就完事
- [ ] 备份：数据库有定时 dump，卷目录知道在哪

## 三、Nginx 反向代理

```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Upgrade $http_upgrade;      # WebSocket
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 300s;                     # 长任务
    }
}
```

常见坑：

- 前端路由刷新 404 → 加 `try_files $uri $uri/ /index.html;`
- 上传大文件 413 → `client_max_body_size 50m;`
- WebSocket 连不上 → 缺 `Upgrade` / `Connection` 头
- 后端拿到的是 127.0.0.1 → 缺 `X-Real-IP` / `X-Forwarded-For`

## 四、HTTPS

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d example.com -d www.example.com
sudo certbot renew --dry-run   # 确认自动续期可用
```

要点：

- 域名必须先解析到这台机器，否则验证失败
- 证书续期是定时任务，一定跑一次 dry-run 确认
- 开了 HTTPS 后，应用内生成的回调地址、静态资源地址要跟着改成 https，否则混合内容被拦

## 五、Docker Compose 模板

```yaml
services:
  app:
    build: .
    restart: unless-stopped
    env_file: .env
    ports:
      - "127.0.0.1:3000:3000"   # 只给本机 Nginx 访问
    depends_on:
      - db

  db:
    image: postgres:16
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - ./data/pg:/var/lib/postgresql/data
```

规则：

- `restart: unless-stopped`，否则重启机器服务全没
- 端口绑定 `127.0.0.1`，只让 Nginx 暴露出去
- 数据必须挂卷，删容器不丢数据
- 别把 `latest` 用在生产，写死版本号

## 六、不用 Docker 的情况

Python：

```bash
gunicorn -w 4 -b 127.0.0.1:8000 app:app     # 或 uvicorn --workers 4
```

Node：

```bash
pm2 start npm --name myapp -- start
pm2 save && pm2 startup                    # 开机自启
```

两者都要配 systemd 或 pm2 startup，**否则 SSH 断开服务就死**。

## 七、排查顺序

"本地能跑、线上不行"按这个顺序查：

1. 进程活没活：`docker ps` / `pm2 list` / `systemctl status`
2. 端口通不通：`curl 127.0.0.1:端口`，再 `curl 公网IP:端口`
3. 容器内部：`docker logs -f --tail 100`、`docker exec -it sh`
4. 网络：安全组 → 防火墙 → Nginx → 应用，逐层 `telnet`/`curl`
5. 环境差异：node/python 版本、依赖锁文件、环境变量、时区

## 八、上线后的基本运维

- 日志轮转：`logrotate` 或 Compose 的 `logging` 限制大小
- 监控：至少一个 `curl` 健康检查 + 磁盘告警
- 备份：`pg_dump` 定时到独立目录，异地存一份
- 回滚：保留上一个镜像 tag 或 git tag，出事能退回

## 九、安全底线

- 不用 root 跑应用，Compose 里指定 `user:`
- 数据库端口不要对公网开放
- SSH 改端口 + 禁密码登录（用密钥）
- 后台管理路径改掉默认值，别留 `/admin` 裸奔
