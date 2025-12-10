# 使用GitHub Actions在线打包APK（最简单方法）

## 为什么选择GitHub Actions？

✅ **完全免费** - GitHub提供免费构建服务  
✅ **无需配置** - 不需要安装任何工具  
✅ **自动构建** - 推送代码自动打包  
✅ **云端运行** - 在GitHub服务器上构建  
✅ **直接下载** - 构建完成后直接下载APK  

## 完整步骤

### 第一步：准备GitHub账号

1. 如果没有GitHub账号，访问 https://github.com 注册
2. 登录账号

### 第二步：创建仓库并上传代码

#### 方法A：使用Git命令行（推荐）

```bash
# 1. 在项目目录初始化Git
git init

# 2. 添加所有文件
git add .

# 3. 提交
git commit -m "Initial commit"

# 4. 在GitHub上创建新仓库（网页操作）
# 访问：https://github.com/new
# 输入仓库名，例如：sensortoolbox
# 不要勾选"Initialize with README"

# 5. 连接远程仓库并推送
git remote add origin https://github.com/你的用户名/sensortoolbox.git
git branch -M main
git push -u origin main
```

#### 方法B：使用GitHub Desktop（图形界面）

1. 下载安装：https://desktop.github.com/
2. 登录GitHub账号
3. File > Add Local Repository
4. 选择项目文件夹
5. Publish repository

#### 方法C：使用网页上传（最简单）

1. 在GitHub创建新仓库
2. 点击"uploading an existing file"
3. 拖拽项目文件夹上传
4. 提交

### 第三步：创建工作流文件

项目已经包含了`.github/workflows/build.yml`文件，如果还没有：

1. 在项目根目录创建`.github/workflows/`文件夹
2. 创建`build.yml`文件（内容已提供）

### 第四步：触发构建

#### 自动触发：
- 推送代码到GitHub会自动触发构建

#### 手动触发：
1. 访问：`https://github.com/你的用户名/仓库名/actions`
2. 点击"Build Android APK"
3. 点击"Run workflow"
4. 选择分支，点击"Run workflow"

### 第五步：下载APK

1. 等待构建完成（约10-30分钟，首次较慢）
2. 点击构建任务
3. 在"Artifacts"部分下载APK
4. 解压下载的zip文件，找到APK

### 第六步：安装到手机

1. **通过USB传输**：
   - 连接手机到电脑
   - 复制APK到手机
   - 在手机上打开文件管理器安装

2. **通过云盘**：
   - 上传APK到百度网盘/OneDrive等
   - 在手机上下载安装

3. **通过微信/QQ**：
   - 发送APK到文件传输助手
   - 在手机上接收并安装

4. **通过ADB安装**（需要USB调试）：
   ```bash
   adb install 下载的APK文件.apk
   ```

## 常见问题

### Q: 构建失败怎么办？
A: 
1. 检查`.github/workflows/build.yml`文件是否正确
2. 查看构建日志，找到错误信息
3. 确保`buildozer.spec`配置正确
4. 检查代码是否有语法错误

### Q: 构建需要多长时间？
A: 
- 首次构建：20-40分钟（需要下载依赖）
- 后续构建：10-20分钟

### Q: 可以设置自动构建吗？
A: 
- 是的，每次push代码都会自动构建
- 也可以设置定时构建（修改workflow文件）

### Q: 构建次数有限制吗？
A: 
- 免费账号：每月2000分钟构建时间
- 对于这个项目，足够使用

### Q: 可以构建Release版本吗？
A: 
- 可以，需要配置签名密钥
- 在GitHub Secrets中添加密钥信息
- 修改workflow使用release模式

## 优化建议

1. **添加.gitignore**：
   ```
   __pycache__/
   *.pyc
   .buildozer/
   bin/
   .python-version
   ```

2. **只构建特定分支**：
   修改workflow，只在main分支构建

3. **缓存依赖**：
   可以添加缓存步骤加速构建

4. **多架构构建**：
   可以同时构建arm64和armeabi-v7a版本

## 下一步

构建成功后，你可以：
1. 下载APK安装到手机测试
2. 分享APK给其他人
3. 发布到应用商店（需要签名）

## 需要帮助？

如果遇到问题：
1. 查看GitHub Actions的构建日志
2. 检查`buildozer.spec`配置
3. 参考Buildozer官方文档
4. 在GitHub Issues中提问

