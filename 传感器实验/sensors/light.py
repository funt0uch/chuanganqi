"""
光线传感器模块
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from plyer import light


class LightSensorScreen(Screen):
    """光线传感器界面"""
    
    def __init__(self, **kwargs):
        super(LightSensorScreen, self).__init__(**kwargs)
        self.setup_ui()
    
    def setup_ui(self):
        """设置用户界面"""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # 标题
        title = Label(
            text='光线传感器',
            font_size=24,
            size_hint_y=None,
            height=50,
            bold=True
        )
        layout.add_widget(title)
        
        # 光线强度显示
        self.label_value = Label(
            text='0',
            font_size=72,
            size_hint_y=None,
            height=150,
            bold=True
        )
        layout.add_widget(self.label_value)
        
        # 单位
        unit_label = Label(
            text='勒克斯 (Lux)',
            font_size=20,
            size_hint_y=None,
            height=40
        )
        layout.add_widget(unit_label)
        
        # 状态显示
        self.label_status = Label(
            text='等待检测...',
            font_size=18,
            size_hint_y=None,
            height=50,
            color=(1, 0.5, 0, 1)
        )
        layout.add_widget(self.label_status)
        
        # 参考值说明
        reference = Label(
            text='光线强度参考值：\n'
                 '• 完全黑暗: 0-1 Lux\n'
                 '• 月光: 0.1-1 Lux\n'
                 '• 室内照明: 100-1000 Lux\n'
                 '• 阳光直射: 10000-100000 Lux',
            font_size=14,
            size_hint_y=None,
            height=150,
            text_size=(None, None),
            halign='left',
            valign='top'
        )
        layout.add_widget(reference)
        
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
            light.enable()
            Clock.schedule_interval(self.update_light, 0.1)
        except Exception as e:
            self.label_value.text = '错误'
            self.label_status.text = f'设备不支持光线传感器: {str(e)}'
    
    def on_leave(self):
        """离开屏幕时停止传感器"""
        try:
            light.disable()
            Clock.unschedule(self.update_light)
        except:
            pass
    
    def update_light(self, dt):
        """更新光线数据"""
        try:
            # Plyer API: light.illumination 返回浮点数或None
            light_value = light.illumination
            if light_value is not None:
                self.label_value.text = f'{light_value:.1f}'
                self.label_status.text = self.get_light_status(light_value)
        except Exception as e:
            self.label_value.text = '错误'
            self.label_status.text = f'读取失败: {str(e)}'
    
    def get_light_status(self, lux):
        """根据光线强度获取状态描述"""
        if lux < 1:
            return '完全黑暗'
        elif lux < 10:
            return '很暗'
        elif lux < 100:
            return '较暗'
        elif lux < 1000:
            return '室内照明'
        elif lux < 10000:
            return '明亮'
        else:
            return '非常明亮（可能为阳光直射）'
    
    def go_back(self, instance):
        """返回主界面"""
        self.on_leave()
        self.manager.current = 'main'

