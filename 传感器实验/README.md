# 传感器工具箱 APP (Python版本)

## 项目简介

本项目是一个基于Python开发的智能手机传感器应用，使用Kivy框架和Plyer库实现跨平台移动应用开发。该应用集成了多种传感器功能，包括加速度传感器、指南针、光线传感器、陀螺仪和方向传感器。

## 功能特性

1. **加速度传感器**
   - 实时显示X、Y、Z三轴加速度值
   - 摇一摇检测功能
   - 震动反馈

2. **指南针**
   - 实时显示设备方向
   - 磁场强度检测
   - 方位角显示

3. **光线传感器**
   - 实时检测环境光线强度（Lux）
   - 光线强度状态提示
   - 参考值说明

4. **陀螺仪**
   - 实时显示X、Y、Z三轴角速度
   - 检测设备旋转

5. **方向传感器**
   - 显示方位角、俯仰角、翻滚角
   - 实时检测设备姿态

## 技术栈

- **开发语言**: Python 3.8+
- **GUI框架**: Kivy 2.1.0+
- **传感器库**: Plyer 2.1.0+
- **打包工具**: Buildozer (Android)
- **目标平台**: Android 8.0+ (API 26+)
- **目标API**: Android 14 (API 34)

## 项目结构

```
传感器实验/
├── main.py                 # 主程序入口
├── sensors/                # 传感器模块目录
│   ├── __init__.py
│   ├── accelerometer.py    # 加速度传感器
│   ├── compass.py          # 指南针
│   ├── light.py            # 光线传感器
│   ├── gyroscope.py        # 陀螺仪
│   └── orientation.py      # 方向传感器
├── requirements.txt        # Python依赖
├── buildozer.spec          # Buildozer配置文件
└── README.md               # 项目说明
```

## 环境配置

### 1. 安装Python依赖

```bash
pip install -r requirements.txt
```

### 2. 桌面测试运行

在Windows/Linux/Mac上可以直接运行进行测试：

```bash
python main.py
```

注意：桌面环境下传感器功能可能无法正常工作，需要使用Android设备。

## Android打包

### 1. 安装Buildozer

**Linux/Mac:**
```bash
pip install buildozer
```

**Windows:**
需要使用WSL (Windows Subsystem for Linux) 或虚拟机

### 2. 安装Android依赖

```bash
# 安装Android SDK和NDK
# 确保已安装Java JDK
```

### 3. 构建APK

```bash
# 首次构建（会下载依赖，耗时较长）
buildozer android debug

# 生成的APK位于 bin/ 目录
```

### 4. 安装到设备

```bash
# 通过ADB安装
adb install bin/sensortoolbox-1.0-arm64-v8a-debug.apk

# 或直接传输APK文件到手机安装
```

## 使用说明

1. **启动应用**: 安装APK后，打开应用进入主界面
2. **选择功能**: 点击相应的按钮进入对应的传感器功能页面
3. **查看数据**: 传感器数据会实时更新显示
4. **返回主界面**: 点击"返回主界面"按钮

## 传感器说明

### 加速度传感器 (Accelerometer)
- 检测设备在X、Y、Z三个方向上的加速度
- 单位：m/s²
- 应用：摇一摇检测、计步器等

### 磁力传感器 (Magnetometer)
- 检测设备周围的磁场强度
- 单位：μT (微特斯拉)
- 应用：指南针、金属检测等

### 光线传感器 (Light Sensor)
- 检测环境光线强度
- 单位：Lux (勒克斯)
- 应用：自动调节屏幕亮度

### 陀螺仪 (Gyroscope)
- 检测设备绕X、Y、Z轴的旋转角速度
- 单位：rad/s (弧度每秒)
- 应用：游戏控制、姿态检测等

### 方向传感器 (Orientation)
- 通过加速度传感器和磁力传感器计算得出
- 包括方位角、俯仰角、翻滚角
- 应用：水平仪、AR应用等

## 开发说明

### 代码结构

- `main.py`: 应用入口，管理屏幕切换
- `sensors/`: 各个传感器功能模块
  - 每个模块都是独立的Screen类
  - 使用Plyer库访问传感器
  - 使用Kivy的Clock定时更新数据

### 添加新传感器

1. 在`sensors/`目录下创建新的Python文件
2. 继承`Screen`类实现传感器界面
3. 在`main.py`中导入并添加到ScreenManager

### 注意事项

1. 部分设备可能不支持所有传感器，应用会进行相应提示
2. 传感器数据会持续更新，可能影响电池续航
3. 使用指南针功能时，建议远离强磁场环境
4. 摇一摇功能需要设备支持震动功能
5. 在桌面环境下测试时，传感器功能可能无法正常工作

## 常见问题

### Q: 桌面运行时报错？
A: 桌面环境下Plyer可能无法访问传感器，这是正常的。需要在Android设备上运行。

### Q: 如何打包APK？
A: 使用Buildozer工具，详见"Android打包"章节。Windows用户需要使用WSL。

### Q: 传感器数据不更新？
A: 检查设备是否支持该传感器，以及是否授予了必要的权限。

## 开发者

- 开发语言：Python
- GUI框架：Kivy
- 传感器库：Plyer
- 打包工具：Buildozer

## 许可证

本项目仅用于学习和教育目的。

## 更新日志

### v1.0 (2024)
- 初始版本发布
- 实现5种传感器功能
- 使用Kivy和Plyer开发
- 支持Android平台打包
