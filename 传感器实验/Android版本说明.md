# Android版本配置说明

## 当前配置

- **最低支持版本**: Android 8.0 (API 26)
- **目标编译版本**: Android 14 (API 34)
- **更新日期**: 2024年

## 版本选择说明

### 为什么选择 API 26 (Android 8.0) 作为最低版本？

1. **更好的兼容性**
   - Android 8.0 (2017年发布) 已经覆盖了绝大多数现有设备
   - 根据2024年的统计数据，Android 8.0+ 的设备占比超过95%

2. **现代化特性支持**
   - API 26 引入了通知渠道、自适应图标等现代Android特性
   - 更好的后台限制和电池优化
   - 更完善的权限管理

3. **开发便利性**
   - 可以使用更现代的API和开发工具
   - 减少对旧版本兼容性的处理工作

4. **传感器功能支持**
   - 所有需要的传感器功能在API 26上都能正常工作
   - 不需要依赖更旧的API特性

### 为什么目标API是 34 (Android 14)？

- Android 14 是2023年发布的最新稳定版本
- 支持最新的安全特性和性能优化
- 确保应用可以在最新设备上正常运行

## Android版本对应关系

| Android版本 | API Level | 发布时间 |
|------------|-----------|----------|
| Android 8.0 | 26 | 2017年 |
| Android 8.1 | 27 | 2017年 |
| Android 9.0 | 28 | 2018年 |
| Android 10 | 29 | 2019年 |
| Android 11 | 30 | 2020年 |
| Android 12 | 31 | 2021年 |
| Android 12L | 32 | 2022年 |
| Android 13 | 33 | 2022年 |
| Android 14 | 34 | 2023年 |
| Android 15 | 35 | 2024年 |

## 如果需要调整版本

### 降低最低版本（兼容更多旧设备）

如果希望支持Android 7.0 (API 24)，可以修改 `buildozer.spec`:

```ini
android.minapi = 24
```

**注意**: 这可能会限制使用某些现代API特性。

### 提高最低版本（使用更多新特性）

如果只支持较新的设备，可以提高到API 28 (Android 9.0) 或更高:

```ini
android.minapi = 28  # Android 9.0
```

### 更新目标API

如果Android 15 (API 35) 正式发布并稳定后，可以更新:

```ini
android.api = 35  # Android 15
```

## 设备兼容性

根据2024年的统计数据：
- **Android 8.0+ (API 26+)**: 覆盖约95%+的设备
- **Android 9.0+ (API 28+)**: 覆盖约90%+的设备
- **Android 10+ (API 29+)**: 覆盖约85%+的设备

当前配置 (API 26+) 可以在绝大多数Android设备上运行。

## 测试建议

1. **最低版本测试**: 在Android 8.0设备上测试所有功能
2. **目标版本测试**: 在Android 14设备上测试最新特性
3. **中间版本测试**: 建议在Android 10-12的设备上测试兼容性

## 参考资料

- [Android API级别](https://developer.android.com/guide/topics/manifest/uses-sdk-element)
- [Android版本分布](https://developer.android.com/about/dashboards)
- [Buildozer配置文档](https://buildozer.readthedocs.io/)



