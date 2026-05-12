---
name: flutter-china-deploy
description: 当用户需要在中国环境部署 Flutter 项目、配置国内镜像加速或解决依赖下载问题时使用。此 Skill 提供 Flutter 项目初始化、部署和运行时的完整镜像配置方案。
dependencies: []
---

# Flutter 中国环境部署加速

## 快速开始

当用户需要部署 Flutter 项目时，按以下步骤执行：

### 1. 设置环境变量镜像

在终端执行或写入 `~/.zshrc`：

```bash
export PUB_HOSTED_URL=https://pub.flutter-io.cn
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn
```

### 2. 项目初始化 (FVM 版)

```bash
fvm install stable
fvm use stable --force
fvm flutter pub get
```

## Gradle 配置优化

### gradle-wrapper.properties

修改 `android/gradle/wrapper/gradle-wrapper.properties`：

```properties
distributionUrl=https\://mirrors.cloud.tencent.com/gradle/gradle-8.10.2-all.zip
```

### settings.gradle.kts

在 `android/settings.gradle.kts` 的 `repositories` 块添加：

```kotlin
repositories {
    maven { url = uri("https://storage.flutter-io.cn/download.flutter.io") }
    maven { url = uri("https://maven.aliyun.com/repository/google") }
    maven { url = uri("https://maven.aliyun.com/repository/public") }
    maven { url = uri("https://maven.aliyun.com/repository/gradle-plugin") }
    google()
    mavenCentral()
}
```

### build.gradle.kts

在 `android/build.gradle.kts` 同样配置 Maven 镜像。

### gradle.properties

在 `android/gradle.properties` 添加优化配置：

```properties
kotlin.compiler.execution.strategy=in-process
org.gradle.daemon=false
android.useAndroidX=true
android.enableJetifier=true
```

## Android SDK 配置

### local.properties

创建或修改 `android/local.properties`：

```properties
sdk.dir=/Volumes/MacOS/Android/sdk
```

### 环境变量

在 `~/.zshrc` 添加：

```bash
export ANDROID_HOME=/Volumes/MacOS/Android/sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
```

## 运行项目

```bash
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn && \
export PUB_HOSTED_URL=https://pub.flutter-io.cn && \
fvm flutter run -d <设备ID>
```

## 常见问题排查

| 错误信息 | 解决方案 |
|---------|---------|
| Timeout waiting to lock build logic queue | `pkill -f gradle` 并删除 `android/.gradle` |
| Could not find io.flutter:... | 检查 `settings.gradle.kts` 是否包含 `download.flutter.io` 镜像 |
| Operation not permitted | 检查 `GRADLE_USER_HOME` 路径权限 |

## 配置脚本

使用 `scripts/configure_mirrors.py` 自动配置：

```bash
# 检查当前配置状态
python3 scripts/configure_mirrors.py --check

# 配置 Shell 环境变量
python3 scripts/configure_mirrors.py --shell

# 配置 Gradle 镜像 (指定项目路径)
python3 scripts/configure_mirrors.py --project /path/to/flutter/project --gradle

# 执行所有配置
python3 scripts/configure_mirrors.py --project /path/to/flutter/project --all
```
