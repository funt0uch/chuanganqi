"""
方向传感器模块
通过加速度传感器和磁力传感器计算设备姿态
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from plyer import accelerometer, magnetometer
import math


class OrientationScreen(Screen):
    """方向传感器界面"""
    
    def __init__(self, **kwargs):
        super(OrientationScreen, self).__init__(**kwargs)
        self.accel_data = None
        self.magnet_data = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """设置用户界面"""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # 标题
        title = Label(
            text='方向传感器',
            font_size=24,
            size_hint_y=None,
            height=50,
            bold=True
        )
        layout.add_widget(title)
        
        # 方位角显示
        self.label_azimuth = Label(
            text='方位角: 0.0°',
            font_size=20,
            size_hint_y=None,
            height=60,
            text_size=(None, None),
            halign='left'
        )
        layout.add_widget(self.label_azimuth)
        
        # 俯仰角显示
        self.label_pitch = Label(
            text='俯仰角: 0.0°',
            font_size=20,
            size_hint_y=None,
            height=60,
            text_size=(None, None),
            halign='left'
        )
        layout.add_widget(self.label_pitch)
        
        # 翻滚角显示
        self.label_roll = Label(
            text='翻滚角: 0.0°',
            font_size=20,
            size_hint_y=None,
            height=60,
            text_size=(None, None),
            halign='left'
        )
        layout.add_widget(self.label_roll)
        
        # 说明
        info = Label(
            text='方位角：设备绕Z轴旋转的角度\n'
                 '俯仰角：设备绕X轴旋转的角度\n'
                 '翻滚角：设备绕Y轴旋转的角度',
            font_size=14,
            size_hint_y=None,
            height=100,
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
            accelerometer.enable()
            magnetometer.enable()
            Clock.schedule_interval(self.update_orientation, 0.1)
        except Exception as e:
            self.label_azimuth.text = f'错误: {str(e)}'
    
    def on_leave(self):
        """离开屏幕时停止传感器"""
        try:
            accelerometer.disable()
            magnetometer.disable()
            Clock.unschedule(self.update_orientation)
        except:
            pass
    
    def update_orientation(self, dt):
        """更新方向数据"""
        try:
            # 获取加速度和磁力数据
            self.accel_data = accelerometer.acceleration
            self.magnet_data = magnetometer.field
            
            if self.accel_data and self.magnet_data and len(self.accel_data) >= 3 and len(self.magnet_data) >= 3:
                azimuth, pitch, roll = self.calculate_orientation(
                    self.accel_data, self.magnet_data
                )
                
                self.label_azimuth.text = f'方位角: {azimuth:.1f}°'
                self.label_pitch.text = f'俯仰角: {pitch:.1f}°'
                self.label_roll.text = f'翻滚角: {roll:.1f}°'
        except Exception as e:
            self.label_azimuth.text = f'错误: {str(e)}'
    
    def calculate_orientation(self, accel, magnet):
        """计算设备姿态角度"""
        ax, ay, az = accel
        mx, my, mz = magnet
        
        # 归一化加速度向量
        norm_a = math.sqrt(ax**2 + ay**2 + az**2)
        if norm_a > 0:
            ax, ay, az = ax/norm_a, ay/norm_a, az/norm_a
        
        # 归一化磁场向量
        norm_m = math.sqrt(mx**2 + my**2 + mz**2)
        if norm_m > 0:
            mx, my, mz = mx/norm_m, my/norm_m, mz/norm_m
        
        # 计算方位角（绕Z轴）
        azimuth = math.atan2(my, mx) * 180 / math.pi
        azimuth = (azimuth + 360) % 360
        
        # 计算俯仰角（绕X轴）
        pitch = math.asin(-ax) * 180 / math.pi
        
        # 计算翻滚角（绕Y轴）
        roll = math.atan2(ay, az) * 180 / math.pi
        
        return azimuth, pitch, roll
    
    def go_back(self, instance):
        """返回主界面"""
        self.on_leave()
        self.manager.current = 'main'

