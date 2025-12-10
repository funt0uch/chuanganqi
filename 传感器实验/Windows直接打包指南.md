# Windows直接打包APK指南（无需虚拟机）

## 方法一：BeeWare Briefcase（推荐⭐）

BeeWare的Briefcase工具可以在Windows上直接打包Android APK，无需虚拟机或WSL。

### 1.1 安装准备

```bash
# 1. 安装Briefcase
pip install briefcase

# 2. 安装Java JDK（如果还没有）
# 下载：https://adoptium.net/
# 选择Windows x64版本

# 3. 安装Android SDK（可选，Briefcase会自动下载）
# 或者手动下载：https://developer.android.com/studio#command-tools
```

### 1.2 配置项目

由于我们的项目是Kivy应用，需要转换为Briefcase格式：

```bash
# 在项目根目录运行
briefcase new

# 按照提示输入：
# - Formal Name: 传感器工具箱
# - App Name: sensortoolbox
# - Bundle: com.sensorlab
# - Project Name: sensortoolbox
```

### 1.3 修改配置

创建`pyproject.toml`文件（如果不存在）：

```toml
[tool.briefcase]
project_name = "sensortoolbox"
bundle = "com.sensorlab"
version = "1.0.0"
url = "https://example.com"
license = "MIT"
author = "Your Name"
author_email = "your@email.com"

[tool.briefcase.app.sensortoolbox]
formal_name = "传感器工具箱"
sources = ["main.py", "sensors"]
requires = ["kivy>=2.1.0", "plyer>=2.1.0"]

[tool.briefcase.app.sensortoolbox.android]
requires = ["kivy>=2.1.0", "plyer>=2.1.0"]
```

### 1.4 打包APK

```bash
# 首次构建（会下载Android SDK等，需要较长时间）
briefcase create android

# 构建APK
briefcase build android

# 打包APK
briefcase package android

# 生成的APK在：android/app/build/outputs/apk/
```

---

## 方法二：在线构建服务（最简单⭐）

### 2.1 GitHub Actions（免费，推荐）

#### 步骤：

1. **创建GitHub仓库**
   - 将项目上传到GitHub

2. **创建GitHub Actions工作流**

   在项目根目录创建：`.github/workflows/build.yml`

   ```yaml
   name: Build Android APK

   on:
     push:
       branches: [ main ]
     workflow_dispatch:

   jobs:
     build:
       runs-on: ubuntu-latest
       
       steps:
       - uses: actions/checkout@v3
       
       - name: Set up Python
         uses: actions/setup-python@v4
         with:
           python-version: '3.9'
       
       - name: Install dependencies
         run: |
           pip install buildozer cython
           sudo apt-get update
           sudo apt-get install -y git unzip openjdk-17-jdk python3-pip
       
       - name: Build APK
         run: |
           buildozer android debug
       
       - name: Upload APK
         uses: actions/upload-artifact@v3
         with:
           name: app-debug
           path: bin/*.apk
   ```

3. **触发构建**
   - 推送代码到GitHub
   - 或者手动触发：Actions > Build Android APK > Run workflow

4. **下载APK**
   - 构建完成后，在Actions页面下载APK文件

### 2.2 GitLab CI/CD（免费）

类似GitHub Actions，在GitLab上创建`.gitlab-ci.yml`：

```yaml
build_apk:
  image: ubuntu:22.04
  before_script:
    - apt-get update
    - apt-get install -y python3-pip git unzip openjdk-17-jdk
    - pip3 install buildozer cython
  script:
    - buildozer android debug
  artifacts:
    paths:
      - bin/*.apk
```

### 2.3 使用现成的在线服务

- **Appetize.io** - 在线Android模拟器（但主要是测试，不是打包）
- **Bitrise** - CI/CD服务（有免费额度）
- **CircleCI** - CI/CD服务（有免费额度）

---

## 方法三：使用Docker（轻量级，不算完整虚拟机）

### 3.1 安装Docker Desktop

1. 下载：https://www.docker.com/products/docker-desktop
2. 安装并启动Docker Desktop

### 3.2 使用Docker构建

创建`Dockerfile`：

```dockerfile
FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3-pip git unzip openjdk-17-jdk && \
    pip3 install buildozer cython

WORKDIR /app
COPY . .

CMD ["buildozer", "android", "debug"]
```

构建命令：

```bash
# 构建镜像
docker build -t kivy-builder .

# 运行构建（挂载当前目录）
docker run -v %cd%:/app kivy-builder

# APK会在项目的bin目录中
```

---

## 方法四：使用Python-for-Android（p4a）

虽然p4a主要支持Linux，但可以尝试在Windows上使用：

```bash
# 安装
pip install python-for-android

# 可能需要安装Android SDK和NDK
# 然后尝试：
p4a create --requirements=kivy,plyer --arch=arm64-v8a
```

**注意**：p4a在Windows上可能不稳定，不推荐。

---

## 推荐方案对比

| 方案 | 难度 | 时间 | 成功率 | 推荐度 |
|------|------|------|--------|--------|
| **GitHub Actions** | ⭐⭐ | 30分钟 | 高 | ⭐⭐⭐⭐⭐ |
| **BeeWare Briefcase** | ⭐⭐⭐ | 1-2小时 | 中 | ⭐⭐⭐⭐ |
| **Docker** | ⭐⭐⭐ | 1小时 | 高 | ⭐⭐⭐ |
| **GitLab CI** | ⭐⭐ | 30分钟 | 高 | ⭐⭐⭐⭐ |

---

## 最推荐：GitHub Actions（免费且简单）

### 快速开始：

1. **创建GitHub仓库**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/你的用户名/传感器实验.git
   git push -u origin main
   ```

2. **创建Actions工作流文件**
   
   创建：`.github/workflows/build.yml`（内容见上面）

3. **推送代码**
   ```bash
   git add .github/workflows/build.yml
   git commit -m "Add build workflow"
   git push
   ```

4. **等待构建完成**
   - 访问：`https://github.com/你的用户名/传感器实验/actions`
   - 点击最新的workflow运行
   - 构建完成后下载APK

5. **传输到手机**
   - 下载APK文件
   - 通过USB、云盘、微信等传输到手机
   - 在手机上安装

---

## 详细步骤：GitHub Actions完整配置

让我为你创建完整的配置文件：

