# GitHub Actions设置步骤

## 在GitHub上设置工作流

当你看到"Get started with GitHub Actions"页面时：

### ✅ 正确操作：

1. **点击 "Skip this and set up a workflow yourself"**
   - 或者直接关闭这个页面
   - 因为我们已经有自定义的workflow文件了

2. **或者选择任意一个模板后删除，使用我们的**

### 📝 详细步骤：

#### 方法一：直接使用我们的workflow（推荐）

1. **跳过模板选择**
   - 点击 "Skip this and set up a workflow yourself"
   - 或者直接访问：`https://github.com/你的用户名/仓库名/actions/new`

2. **创建workflow文件**
   - 点击 "set up a workflow yourself"
   - 文件名输入：`build.yml`
   - 删除默认内容
   - 复制我们项目中的`.github/workflows/build.yml`内容

3. **或者直接上传文件**
   - 在本地项目已经有`.github/workflows/build.yml`文件
   - 直接上传整个项目文件夹即可

#### 方法二：如果已经选择了模板

1. **删除模板内容**
   - 点击创建的文件
   - 删除所有内容

2. **使用我们的配置**
   - 复制`.github/workflows/build.yml`的内容
   - 粘贴并保存

## 验证workflow是否正确

创建后，检查文件内容应该包含：

```yaml
name: Build Android APK

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    # ... 其他配置
```

## 触发构建

### 自动触发：
- 推送代码到main/master分支会自动触发

### 手动触发：
1. 访问：`https://github.com/你的用户名/仓库名/actions`
2. 点击左侧 "Build Android APK"
3. 点击右侧 "Run workflow"
4. 选择分支，点击绿色按钮

## 常见问题

### Q: 我选择了Python模板怎么办？
A: 没关系，可以删除模板内容，使用我们的build.yml配置

### Q: 找不到workflow文件？
A: 
- 确保文件路径是：`.github/workflows/build.yml`
- 文件名必须是`.yml`或`.yaml`结尾
- 文件必须在仓库根目录的`.github/workflows/`文件夹下

### Q: 如何确认workflow已创建？
A:
- 访问仓库页面
- 点击 "Actions" 标签
- 应该能看到 "Build Android APK" 工作流

## 下一步

1. ✅ 创建/确认workflow文件
2. ✅ 推送代码到GitHub
3. ⏳ 等待构建完成（10-30分钟）
4. 📥 下载APK文件
5. 📱 安装到手机

## 快速检查清单

- [ ] 已创建`.github/workflows/build.yml`文件
- [ ] 文件内容包含"Build Android APK"
- [ ] 已推送代码到GitHub
- [ ] 在Actions页面能看到workflow
- [ ] 构建已开始或可以手动触发

