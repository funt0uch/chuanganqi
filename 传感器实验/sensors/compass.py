"""
指南针模块
使用加速度传感器和磁力传感器计算方向
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from plyer import accelerometer, magnetometer
import math


class CompassScreen(Screen):
    """指南针界面"""
    
    def __init__(self, **kwargs):
        super(CompassScreen, self).__init__(**kwargs)
        self.accel_data = None
        self.magnet_data = None
        self.current_degree = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        """设置用户界面"""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # 标题
        title = Label(
            text='指南针',
            font_size=24,
            size_hint_y=None,
            height=50,
            bold=True
        )
        layout.add_widget(title)
        
        # 方向显示
        self.label_direction = Label(
            text='0°',
            font_size=48,
            size_hint_y=None,
            height=100,
            bold=True
        )
        layout.add_widget(self.label_direction)
        
        # 方位角显示
        self.label_azimuth = Label(
            text='方位角: 0°',
            font_size=18,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.label_azimuth)
        
        # 磁场强度显示
        self.label_magnetic = Label(
            text='磁场强度: 0 μT',
            font_size=18,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.label_magnetic)
        
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
            Clock.schedule_interval(self.update_compass, 0.1)
        except Exception as e:
            self.label_direction.text = f'错误: {str(e)}'
    
    def on_leave(self):
        """离开屏幕时停止传感器"""
        try:
            accelerometer.disable()
            magnetometer.disable()
            Clock.unschedule(self.update_compass)
        except:
            pass
    
    def update_compass(self, dt):
        """更新指南针数据"""
        try:
            # 获取加速度和磁力数据
            self.accel_data = accelerometer.acceleration
            self.magnet_data = magnetometer.field
            
            if self.accel_data and self.magnet_data and len(self.accel_data) >= 3 and len(self.magnet_data) >= 3:
                # 计算方位角
                azimuth = self.calculate_azimuth(self.accel_data, self.magnet_data)
                
                # 更新显示
                direction = self.get_direction(azimuth)
                self.label_direction.text = f'{direction}\n{azimuth:.1f}°'
                self.label_azimuth.text = f'方位角: {azimuth:.1f}°'
                
                # 计算磁场强度
                mx, my, mz = self.magnet_data
                magnetic_strength = math.sqrt(mx**2 + my**2 + mz**2)
                self.label_magnetic.text = f'磁场强度: {magnetic_strength:.2f} μT'
        except Exception as e:
            self.label_direction.text = f'错误: {str(e)}'
    
    def calculate_azimuth(self, accel, magnet):
        """计算方位角"""
        ax, ay, az = accel
        mx, my, mz = magnet
        
        # 归一化加速度向量
        norm = math.sqrt(ax**2 + ay**2 + az**2)
        if norm > 0:
            ax, ay, az = ax/norm, ay/norm, az/norm
        
        # 计算旋转矩阵
        # 简化计算，使用反正切函数
        azimuth = math.atan2(my, mx) * 180 / math.pi
        azimuth = (azimuth + 360) % 360
        
        return azimuth
    
    def get_direction(self, azimuth):
        """根据方位角获取方向"""
        directions = ['北', '东北', '东', '东南', '南', '西南', '西', '西北']
        index = int((azimuth + 22.5) / 45) % 8
        return directions[index]
    
    def go_back(self, instance):
        """返回主界面"""
        self.on_leave()
        self.manager.current = 'main'

