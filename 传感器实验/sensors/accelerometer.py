"""
加速度传感器模块
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from plyer import accelerometer, vibrator
import math


class AccelerometerScreen(Screen):
    """加速度传感器界面"""
    
    def __init__(self, **kwargs):
        super(AccelerometerScreen, self).__init__(**kwargs)
        self.is_monitoring = False
        self.last_x = 0
        self.last_y = 0
        self.last_z = 0
        self.last_update_time = 0
        self.shake_threshold = 15
        self.time_threshold = 200  # 毫秒
        
        self.setup_ui()
    
    def setup_ui(self):
        """设置用户界面"""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # 标题
        title = Label(
            text='加速度传感器',
            font_size=24,
            size_hint_y=None,
            height=50,
            bold=True
        )
        layout.add_widget(title)
        
        # 数据显示区域
        self.label_x = Label(
            text='X: 0.00 m/s²',
            font_size=20,
            size_hint_y=None,
            height=60,
            text_size=(None, None),
            halign='left'
        )
        layout.add_widget(self.label_x)
        
        self.label_y = Label(
            text='Y: 0.00 m/s²',
            font_size=20,
            size_hint_y=None,
            height=60,
            text_size=(None, None),
            halign='left'
        )
        layout.add_widget(self.label_y)
        
        self.label_z = Label(
            text='Z: 0.00 m/s²',
            font_size=20,
            size_hint_y=None,
            height=60,
            text_size=(None, None),
            halign='left'
        )
        layout.add_widget(self.label_z)
        
        # 摇一摇提示
        self.label_shake = Label(
            text='检测到摇动！',
            font_size=18,
            size_hint_y=None,
            height=50,
            color=(1, 0, 0, 1),
            opacity=0
        )
        layout.add_widget(self.label_shake)
        
        # 控制按钮
        self.btn_control = Button(
            text='开始',
            size_hint_y=None,
            height=50,
            font_size=18
        )
        self.btn_control.bind(on_press=self.toggle_monitoring)
        layout.add_widget(self.btn_control)
        
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
    
    def toggle_monitoring(self, instance):
        """切换监控状态"""
        if not self.is_monitoring:
            self.start_monitoring()
        else:
            self.stop_monitoring()
    
    def start_monitoring(self):
        """开始监控"""
        try:
            accelerometer.enable()
            self.is_monitoring = True
            self.btn_control.text = '停止'
            Clock.schedule_interval(self.update_accelerometer, 0.1)
        except Exception as e:
            self.label_x.text = f'错误: {str(e)}'
    
    def stop_monitoring(self):
        """停止监控"""
        try:
            accelerometer.disable()
            Clock.unschedule(self.update_accelerometer)
            self.is_monitoring = False
            self.btn_control.text = '开始'
            self.label_x.text = 'X: 0.00 m/s²'
            self.label_y.text = 'Y: 0.00 m/s²'
            self.label_z.text = 'Z: 0.00 m/s²'
            self.label_shake.opacity = 0
        except Exception as e:
            pass
    
    def update_accelerometer(self, dt):
        """更新加速度数据"""
        try:
            # Plyer API: accelerometer.acceleration 返回 (x, y, z) 或 None
            accel_data = accelerometer.acceleration
            if accel_data and len(accel_data) >= 3:
                x, y, z = accel_data
                
                self.label_x.text = f'X: {x:.2f} m/s²'
                self.label_y.text = f'Y: {y:.2f} m/s²'
                self.label_z.text = f'Z: {z:.2f} m/s²'
                
                # 摇一摇检测
                import time
                current_time = time.time() * 1000
                if self.last_update_time > 0:
                    diff_time = current_time - self.last_update_time
                    if diff_time > self.time_threshold:
                        speed = abs(x + y + z - self.last_x - self.last_y - self.last_z) / diff_time * 10000
                        
                        if speed > self.shake_threshold:
                            self.label_shake.opacity = 1
                            try:
                                vibrator.vibrate(0.2)  # 震动0.2秒
                            except:
                                pass
                        else:
                            self.label_shake.opacity = 0
                
                self.last_x = x
                self.last_y = y
                self.last_z = z
                self.last_update_time = current_time
        except Exception as e:
            self.label_x.text = f'错误: {str(e)}'
    
    def go_back(self, instance):
        """返回主界面"""
        self.stop_monitoring()
        self.manager.current = 'main'
    
    def on_leave(self):
        """离开屏幕时停止监控"""
        self.stop_monitoring()

