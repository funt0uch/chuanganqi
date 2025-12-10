"""
传感器工具箱 - 主程序
使用Kivy和Plyer开发智能手机传感器应用
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.clock import Clock

# 导入各个传感器模块
from sensors.accelerometer import AccelerometerScreen
from sensors.compass import CompassScreen
from sensors.light import LightSensorScreen
from sensors.gyroscope import GyroscopeScreen
from sensors.orientation import OrientationScreen


class MainScreen(Screen):
    """主界面"""
    
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # 标题
        title = Label(
            text='传感器工具箱',
            font_size=32,
            size_hint_y=None,
            height=60,
            bold=True
        )
        main_layout.add_widget(title)
        
        # 副标题
        subtitle = Label(
            text='选择要使用的传感器功能',
            font_size=16,
            size_hint_y=None,
            height=40
        )
        main_layout.add_widget(subtitle)
        
        # 滚动视图
        scroll = ScrollView()
        content = BoxLayout(orientation='vertical', spacing=15, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))
        
        # 传感器功能按钮
        sensors = [
            ('加速度传感器', 'accelerometer', '检测加速度、摇一摇功能'),
            ('指南针', 'compass', '显示设备方向、指南针'),
            ('光线传感器', 'light', '检测环境光线强度'),
            ('陀螺仪', 'gyroscope', '检测设备旋转角速度'),
            ('方向传感器', 'orientation', '检测设备姿态角度'),
        ]
        
        for name, screen_name, desc in sensors:
            btn = Button(
                text=f'{name}\n{desc}',
                size_hint_y=None,
                height=100,
                font_size=18,
                halign='left',
                valign='middle',
                text_size=(None, None),
                padding=(20, 20)
            )
            btn.bind(on_press=lambda instance, s=screen_name: self.switch_screen(s))
            content.add_widget(btn)
        
        scroll.add_widget(content)
        main_layout.add_widget(scroll)
        
        self.add_widget(main_layout)
    
    def switch_screen(self, screen_name):
        """切换到指定屏幕"""
        self.manager.current = screen_name


class SensorToolboxApp(App):
    """主应用类"""
    
    def build(self):
        # 设置窗口大小（用于桌面测试）
        Window.size = (400, 700)
        
        # 创建屏幕管理器
        sm = ScreenManager()
        
        # 添加主屏幕
        sm.add_widget(MainScreen(name='main'))
        
        # 添加各个传感器屏幕
        sm.add_widget(AccelerometerScreen(name='accelerometer'))
        sm.add_widget(CompassScreen(name='compass'))
        sm.add_widget(LightSensorScreen(name='light'))
        sm.add_widget(GyroscopeScreen(name='gyroscope'))
        sm.add_widget(OrientationScreen(name='orientation'))
        
        return sm


if __name__ == '__main__':
    SensorToolboxApp().run()





