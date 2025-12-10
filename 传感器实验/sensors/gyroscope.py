"""
陀螺仪模块
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from plyer import gyroscope


class GyroscopeScreen(Screen):
    """陀螺仪界面"""
    
    def __init__(self, **kwargs):
        super(GyroscopeScreen, self).__init__(**kwargs)
        self.setup_ui()
    
    def setup_ui(self):
        """设置用户界面"""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # 标题
        title = Label(
            text='陀螺仪',
            font_size=24,
            size_hint_y=None,
            height=50,
            bold=True
        )
        layout.add_widget(title)
        
        # X轴显示
        self.label_x = Label(
            text='X: 0.000 rad/s',
            font_size=20,
            size_hint_y=None,
            height=60,
            text_size=(None, None),
            halign='left'
        )
        layout.add_widget(self.label_x)
        
        # Y轴显示
        self.label_y = Label(
            text='Y: 0.000 rad/s',
            font_size=20,
            size_hint_y=None,
            height=60,
            text_size=(None, None),
            halign='left'
        )
        layout.add_widget(self.label_y)
        
        # Z轴显示
        self.label_z = Label(
            text='Z: 0.000 rad/s',
            font_size=20,
            size_hint_y=None,
            height=60,
            text_size=(None, None),
            halign='left'
        )
        layout.add_widget(self.label_z)
        
        # 说明
        info = Label(
            text='陀螺仪用于检测设备绕X、Y、Z轴的旋转角速度',
            font_size=14,
            size_hint_y=None,
            height=80,
            text_size=(None, None),
            halign='center'
        )
        layout.add_widget(info)
        
        # 返回按钮
        btn_back = Button(
            text='返回主界面',
            size_hint_y=None,
            height=50,
            font_size=18
        )
        btn_back.bind(on_press=self.go_back)
        layout.add_widget(btn_back)
        
        self.add_widget(layout)
    
    def on_enter(self):
        """进入屏幕时启动传感器"""
        try:
            gyroscope.enable()
            Clock.schedule_interval(self.update_gyroscope, 0.1)
        except Exception as e:
            self.label_x.text = f'错误: {str(e)}'
    
    def on_leave(self):
        """离开屏幕时停止传感器"""
        try:
            gyroscope.disable()
            Clock.unschedule(self.update_gyroscope)
        except:
            pass
    
    def update_gyroscope(self, dt):
        """更新陀螺仪数据"""
        try:
            # Plyer API: gyroscope.rotation 返回 (x, y, z) 或 None
            gyro_data = gyroscope.rotation
            if gyro_data and len(gyro_data) >= 3:
                x, y, z = gyro_data
                self.label_x.text = f'X: {x:.3f} rad/s'
                self.label_y.text = f'Y: {y:.3f} rad/s'
                self.label_z.text = f'Z: {z:.3f} rad/s'
        except Exception as e:
            self.label_x.text = f'错误: {str(e)}'
    
    def go_back(self, instance):
        """返回主界面"""
        self.on_leave()
        self.manager.current = 'main'

