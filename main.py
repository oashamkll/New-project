from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, RoundedRectangle, Line, Rectangle
from kivy.metrics import dp, sp
from kivy.utils import platform
from random import randint

# Настройка окна
if platform == 'android':
    Window.fullscreen = 'auto'
else:
    Window.size = (1280, 720)

Builder.load_string('''
#:import dp kivy.metrics.dp
#:import sp kivy.metrics.sp

<GradientButton@Button>:
    btn_color: [0.3, 0.6, 0.9, 1]
    background_color: 0, 0, 0, 0
    background_normal: ''
    font_size: sp(18)
    bold: True
    color: 1, 1, 1, 1
    text_size: self.width - dp(10), self.height
    halign: 'center'
    valign: 'middle'
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.4
        RoundedRectangle:
            pos: self.x + dp(4), self.y - dp(4)
            size: self.size
            radius: [dp(18)]
        Color:
            rgba: self.btn_color if len(self.btn_color) == 4 else [0.3, 0.6, 0.9, 1]
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(18)]
        Color:
            rgba: 1, 1, 1, 0.12
        RoundedRectangle:
            pos: self.x + dp(3), self.y + self.height * 0.5
            size: self.width - dp(6), self.height * 0.45
            radius: [dp(16), dp(16), 0, 0]

<StyledCard@FloatLayout>:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.5
        RoundedRectangle:
            pos: self.x + dp(6), self.y - dp(6)
            size: self.size
            radius: [dp(30)]
        Color:
            rgba: 0.08, 0.08, 0.15, 0.98
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(30)]
        Color:
            rgba: 0.4, 0.6, 1, 0.25
        Line:
            rounded_rectangle: (self.x, self.y, self.width, self.height, dp(30))
            width: dp(2)

<MenuScreen>:
    canvas.before:
        Color:
            rgba: 0.02, 0.02, 0.08, 1
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: 0.1, 0.3, 0.6, 0.35
        Ellipse:
            pos: self.width * 0.5, self.height * 0.05
            size: self.width * 0.6, self.width * 0.6
        Color:
            rgba: 0.5, 0.1, 0.5, 0.25
        Ellipse:
            pos: -self.width * 0.2, self.height * 0.4
            size: self.width * 0.5, self.width * 0.5
    
    FloatLayout:
        StyledCard:
            size_hint: 0.42, 0.88
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
            Label:
                text: "ПОНГ"
                font_size: sp(58)
                bold: True
                color: 1, 0.85, 0.1, 1
                pos_hint: {'center_x': 0.5, 'center_y': 0.85}
                
            Label:
                text: "Классическая аркада"
                font_size: sp(15)
                color: 0.6, 0.65, 0.75, 1
                pos_hint: {'center_x': 0.5, 'center_y': 0.72}
            
            GradientButton:
                text: "ИГРАТЬ"
                font_size: sp(24)
                size_hint: 0.72, 0.13
                pos_hint: {'center_x': 0.5, 'center_y': 0.54}
                btn_color: [0.15, 0.7, 0.35, 1]
                on_release: root.start_game()
                
            GradientButton:
                text: "НАСТРОЙКИ"
                font_size: sp(18)
                size_hint: 0.72, 0.11
                pos_hint: {'center_x': 0.5, 'center_y': 0.38}
                btn_color: [0.2, 0.5, 0.85, 1]
                on_release: root.show_settings()
                
            GradientButton:
                text: "ИНФОРМАЦИЯ"
                font_size: sp(18)
                size_hint: 0.72, 0.11
                pos_hint: {'center_x': 0.5, 'center_y': 0.23}
                btn_color: [0.55, 0.3, 0.7, 1]
                on_release: root.show_info()

<SettingsScreen>:
    canvas.before:
        Color:
            rgba: 0.02, 0.02, 0.08, 1
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: 0.1, 0.25, 0.5, 0.3
        Ellipse:
            pos: self.width * 0.4, self.height * 0.15
            size: self.width * 0.6, self.width * 0.6
    
    FloatLayout:
        StyledCard:
            size_hint: 0.78, 0.92
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
            Label:
                text: "НАСТРОЙКИ"
                font_size: sp(34)
                bold: True
                color: 1, 0.85, 0.1, 1
                pos_hint: {'center_x': 0.5, 'center_y': 0.93}
            
            Label:
                text: "Сложность ИИ:"
                font_size: sp(15)
                color: 0.85, 0.85, 0.92, 1
                pos_hint: {'x': 0.04, 'center_y': 0.80}
                size_hint_x: 0.28
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                
            GradientButton:
                id: easy_btn
                text: "Легко"
                font_size: sp(13)
                size_hint: 0.18, 0.085
                pos_hint: {'center_x': 0.43, 'center_y': 0.80}
                btn_color: root.get_diff_color('easy')
                on_release: root.set_difficulty('easy')
                
            GradientButton:
                id: medium_btn
                text: "Средне"
                font_size: sp(13)
                size_hint: 0.18, 0.085
                pos_hint: {'center_x': 0.62, 'center_y': 0.80}
                btn_color: root.get_diff_color('medium')
                on_release: root.set_difficulty('medium')
                
            GradientButton:
                id: hard_btn
                text: "Сложно"
                font_size: sp(13)
                size_hint: 0.18, 0.085
                pos_hint: {'center_x': 0.81, 'center_y': 0.80}
                btn_color: root.get_diff_color('hard')
                on_release: root.set_difficulty('hard')
            
            Label:
                text: "Скорость мяча:"
                font_size: sp(15)
                color: 0.85, 0.85, 0.92, 1
                pos_hint: {'x': 0.04, 'center_y': 0.66}
                size_hint_x: 0.28
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                
            GradientButton:
                id: slow_btn
                text: "Медленно"
                font_size: sp(11)
                size_hint: 0.18, 0.085
                pos_hint: {'center_x': 0.43, 'center_y': 0.66}
                btn_color: root.get_speed_color('slow')
                on_release: root.set_speed('slow')
                
            GradientButton:
                id: normal_btn
                text: "Обычно"
                font_size: sp(13)
                size_hint: 0.18, 0.085
                pos_hint: {'center_x': 0.62, 'center_y': 0.66}
                btn_color: root.get_speed_color('normal')
                on_release: root.set_speed('normal')
                
            GradientButton:
                id: fast_btn
                text: "Быстро"
                font_size: sp(13)
                size_hint: 0.18, 0.085
                pos_hint: {'center_x': 0.81, 'center_y': 0.66}
                btn_color: root.get_speed_color('fast')
                on_release: root.set_speed('fast')
            
            Label:
                text: "Цвет мяча:"
                font_size: sp(15)
                color: 0.85, 0.85, 0.92, 1
                pos_hint: {'x': 0.04, 'center_y': 0.52}
                size_hint_x: 0.28
                text_size: self.size
                halign: 'left'
                valign: 'middle'
            
            ColorCircle:
                circle_color: [1, 1, 1, 1]
                pos_hint: {'center_x': 0.38, 'center_y': 0.52}
                on_release: root.set_ball_color('white')
                
            ColorCircle:
                circle_color: [1, 0.8, 0, 1]
                pos_hint: {'center_x': 0.48, 'center_y': 0.52}
                on_release: root.set_ball_color('yellow')
                
            ColorCircle:
                circle_color: [0, 1, 0.85, 1]
                pos_hint: {'center_x': 0.58, 'center_y': 0.52}
                on_release: root.set_ball_color('cyan')
                
            ColorCircle:
                circle_color: [1, 0.4, 0.7, 1]
                pos_hint: {'center_x': 0.68, 'center_y': 0.52}
                on_release: root.set_ball_color('pink')
                
            ColorCircle:
                circle_color: [0.4, 1, 0.3, 1]
                pos_hint: {'center_x': 0.78, 'center_y': 0.52}
                on_release: root.set_ball_color('green')
            
            Label:
                text: "Очки для победы:"
                font_size: sp(15)
                color: 0.85, 0.85, 0.92, 1
                pos_hint: {'x': 0.04, 'center_y': 0.38}
                size_hint_x: 0.28
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                
            GradientButton:
                id: pts5_btn
                text: "5"
                font_size: sp(15)
                size_hint: 0.1, 0.085
                pos_hint: {'center_x': 0.40, 'center_y': 0.38}
                btn_color: root.get_points_color(5)
                on_release: root.set_win_points(5)
                
            GradientButton:
                id: pts10_btn
                text: "10"
                font_size: sp(15)
                size_hint: 0.1, 0.085
                pos_hint: {'center_x': 0.52, 'center_y': 0.38}
                btn_color: root.get_points_color(10)
                on_release: root.set_win_points(10)
                
            GradientButton:
                id: pts15_btn
                text: "15"
                font_size: sp(15)
                size_hint: 0.1, 0.085
                pos_hint: {'center_x': 0.64, 'center_y': 0.38}
                btn_color: root.get_points_color(15)
                on_release: root.set_win_points(15)
                
            GradientButton:
                id: pts20_btn
                text: "20"
                font_size: sp(15)
                size_hint: 0.1, 0.085
                pos_hint: {'center_x': 0.76, 'center_y': 0.38}
                btn_color: root.get_points_color(20)
                on_release: root.set_win_points(20)
            
            Label:
                text: "Размер ракетки:"
                font_size: sp(15)
                color: 0.85, 0.85, 0.92, 1
                pos_hint: {'x': 0.04, 'center_y': 0.24}
                size_hint_x: 0.28
                text_size: self.size
                halign: 'left'
                valign: 'middle'
                
            GradientButton:
                id: paddle_small
                text: "Малая"
                font_size: sp(12)
                size_hint: 0.15, 0.085
                pos_hint: {'center_x': 0.42, 'center_y': 0.24}
                btn_color: root.get_paddle_color('small')
                on_release: root.set_paddle_size('small')
                
            GradientButton:
                id: paddle_normal
                text: "Обычная"
                font_size: sp(12)
                size_hint: 0.15, 0.085
                pos_hint: {'center_x': 0.59, 'center_y': 0.24}
                btn_color: root.get_paddle_color('normal')
                on_release: root.set_paddle_size('normal')
                
            GradientButton:
                id: paddle_large
                text: "Большая"
                font_size: sp(12)
                size_hint: 0.15, 0.085
                pos_hint: {'center_x': 0.76, 'center_y': 0.24}
                btn_color: root.get_paddle_color('large')
                on_release: root.set_paddle_size('large')
            
            GradientButton:
                text: "НАЗАД"
                font_size: sp(17)
                size_hint: 0.3, 0.085
                pos_hint: {'center_x': 0.5, 'center_y': 0.08}
                btn_color: [0.65, 0.2, 0.25, 1]
                on_release: root.go_back()

<ColorCircle@Button>:
    circle_color: [1, 1, 1, 1]
    background_color: 0, 0, 0, 0
    background_normal: ''
    size_hint: None, None
    size: dp(46), dp(46)
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.5
        Ellipse:
            pos: self.x + dp(3), self.y - dp(3)
            size: self.size
        Color:
            rgba: self.circle_color if len(self.circle_color) == 4 else [1,1,1,1]
        Ellipse:
            pos: self.pos
            size: self.size
        Color:
            rgba: 1, 1, 1, 0.35
        Ellipse:
            pos: self.x + self.width * 0.22, self.y + self.height * 0.5
            size: self.width * 0.3, self.height * 0.25

<InfoScreen>:
    canvas.before:
        Color:
            rgba: 0.02, 0.02, 0.08, 1
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: 0.4, 0.15, 0.5, 0.25
        Ellipse:
            pos: self.width * 0.55, self.height * 0.1
            size: self.width * 0.5, self.width * 0.5
    
    FloatLayout:
        StyledCard:
            size_hint: 0.48, 0.88
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
            Label:
                text: "ИНФОРМАЦИЯ"
                font_size: sp(32)
                bold: True
                color: 1, 0.85, 0.1, 1
                pos_hint: {'center_x': 0.5, 'center_y': 0.9}
            
            FloatLayout:
                size_hint: 0.9, 0.24
                pos_hint: {'center_x': 0.5, 'center_y': 0.68}
                canvas.before:
                    Color:
                        rgba: 0.1, 0.1, 0.2, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(16)]
                
                Label:
                    text: "Разработчик"
                    font_size: sp(13)
                    color: 0.55, 0.55, 0.65, 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.8}
                    
                Label:
                    text: "@PaceHoz"
                    font_size: sp(24)
                    bold: True
                    color: 0.35, 0.8, 1, 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.48}
                    
                Label:
                    text: "Telegram"
                    font_size: sp(11)
                    color: 0.45, 0.45, 0.55, 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.18}
            
            FloatLayout:
                size_hint: 0.9, 0.32
                pos_hint: {'center_x': 0.5, 'center_y': 0.36}
                canvas.before:
                    Color:
                        rgba: 0.1, 0.1, 0.2, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(16)]
                
                Label:
                    text: "Как играть"
                    font_size: sp(13)
                    color: 0.55, 0.55, 0.65, 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.85}
                    
                Label:
                    text: "Касайтесь ПРАВОЙ стороны\\nчтобы управлять ракеткой"
                    font_size: sp(13)
                    color: 1, 1, 1, 0.9
                    pos_hint: {'center_x': 0.5, 'center_y': 0.55}
                    halign: 'center'
                    
                Label:
                    text: "Первый набравший нужное\\nколичество очков побеждает!"
                    font_size: sp(12)
                    color: 1, 0.85, 0.25, 1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.22}
                    halign: 'center'
            
            GradientButton:
                text: "НАЗАД"
                font_size: sp(17)
                size_hint: 0.38, 0.085
                pos_hint: {'center_x': 0.5, 'center_y': 0.08}
                btn_color: [0.65, 0.2, 0.25, 1]
                on_release: root.go_back()

<GameScreen>:
    PongGame:
        id: pong_game

<WinScreen>:
    canvas.before:
        Color:
            rgba: 0.02, 0.02, 0.08, 1
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: 0.1, 0.4, 0.2, 0.25
        Ellipse:
            pos: self.width * 0.3, self.height * 0.2
            size: self.width * 0.5, self.width * 0.5
    
    FloatLayout:
        StyledCard:
            size_hint: 0.44, 0.72
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
            Label:
                id: win_title
                text: "ПОБЕДА!"
                font_size: sp(40)
                bold: True
                color: 0.3, 1, 0.45, 1
                pos_hint: {'center_x': 0.5, 'center_y': 0.82}
                
            Label:
                id: win_score
                text: "10 : 5"
                font_size: sp(28)
                color: 1, 1, 1, 0.92
                pos_hint: {'center_x': 0.5, 'center_y': 0.62}
            
            GradientButton:
                text: "ИГРАТЬ СНОВА"
                font_size: sp(17)
                size_hint: 0.65, 0.11
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                btn_color: [0.15, 0.7, 0.35, 1]
                on_release: root.play_again()
                
            GradientButton:
                text: "МЕНЮ"
                font_size: sp(15)
                size_hint: 0.5, 0.09
                pos_hint: {'center_x': 0.5, 'center_y': 0.22}
                btn_color: [0.5, 0.3, 0.65, 1]
                on_release: root.go_to_menu()

<PausePopup>:
    title: ''
    separator_height: 0
    background: ''
    background_color: 0, 0, 0, 0
    size_hint: 0.36, 0.52
    auto_dismiss: False
    
    canvas.before:
        Color:
            rgba: 0, 0, 0, 0.85
        Rectangle:
            pos: -5000, -5000
            size: 10000, 10000
        Color:
            rgba: 0.06, 0.06, 0.15, 0.98
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(24)]
    
    FloatLayout:
        Label:
            text: "ПАУЗА"
            font_size: sp(28)
            bold: True
            color: 1, 0.85, 0.15, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.85}
            
        GradientButton:
            text: "ПРОДОЛЖИТЬ"
            font_size: sp(15)
            size_hint: 0.72, 0.13
            pos_hint: {'center_x': 0.5, 'center_y': 0.62}
            btn_color: [0.15, 0.7, 0.35, 1]
            on_release: root.resume()
            
        GradientButton:
            text: "ЗАНОВО"
            font_size: sp(14)
            size_hint: 0.72, 0.11
            pos_hint: {'center_x': 0.5, 'center_y': 0.42}
            btn_color: [0.25, 0.5, 0.8, 1]
            on_release: root.restart()
            
        GradientButton:
            text: "МЕНЮ"
            font_size: sp(14)
            size_hint: 0.72, 0.11
            pos_hint: {'center_x': 0.5, 'center_y': 0.22}
            btn_color: [0.65, 0.22, 0.28, 1]
            on_release: root.to_menu()
''')


class GameSettings:
    """Настройки игры"""
    difficulty = 'medium'
    ball_speed = 'normal'
    ball_color = 'white'
    win_points = 10
    paddle_size = 'normal'
    
    @classmethod
    def get_ai_speed(cls):
        speeds = {'easy': 5, 'medium': 8, 'hard': 13}
        return speeds.get(cls.difficulty, 8)
    
    @classmethod
    def get_ball_speed(cls):
        speeds = {'slow': 10, 'normal': 14, 'fast': 20}
        return speeds.get(cls.ball_speed, 14)
    
    @classmethod
    def get_ball_rgba(cls):
        colors = {
            'white': (1, 1, 1, 1),
            'yellow': (1, 0.8, 0, 1),
            'cyan': (0, 1, 0.85, 1),
            'pink': (1, 0.4, 0.7, 1),
            'green': (0.4, 1, 0.3, 1)
        }
        return colors.get(cls.ball_color, (1, 1, 1, 1))
    
    @classmethod
    def get_paddle_height(cls):
        sizes = {'small': dp(60), 'normal': dp(85), 'large': dp(115)}
        return sizes.get(cls.paddle_size, dp(85))


class PausePopup(Popup):
    """Всплывающее окно паузы"""
    def __init__(self, game, **kwargs):
        super().__init__(**kwargs)
        self.game = game
    
    def resume(self):
        self.dismiss()
        self.game.resume_game()
    
    def restart(self):
        self.dismiss()
        self.game.reset_game()
    
    def to_menu(self):
        self.dismiss()
        self.game.go_to_menu()


class MenuScreen(Screen):
    """Главное меню"""
    def start_game(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'game'
        Clock.schedule_once(lambda dt: self.manager.get_screen('game').ids.pong_game.reset_game(), 0.1)
        
    def show_info(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'info'
        
    def show_settings(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'settings'


class SettingsScreen(Screen):
    """Экран настроек"""
    
    # Цвета по умолчанию
    active_color = [0.18, 0.78, 0.42, 1]
    inactive_color = [0.22, 0.22, 0.32, 1]
    
    def get_diff_color(self, level):
        return self.active_color if GameSettings.difficulty == level else self.inactive_color
    
    def get_speed_color(self, speed):
        active = [0.28, 0.62, 0.92, 1]
        return active if GameSettings.ball_speed == speed else self.inactive_color
    
    def get_points_color(self, points):
        active = [0.85, 0.5, 0.18, 1]
        return active if GameSettings.win_points == points else self.inactive_color
    
    def get_paddle_color(self, size):
        active = [0.7, 0.35, 0.7, 1]
        return active if GameSettings.paddle_size == size else self.inactive_color
    
    def on_enter(self):
        Clock.schedule_once(lambda dt: self.update_buttons(), 0.05)
    
    def update_buttons(self):
        try:
            self.ids.easy_btn.btn_color = self.get_diff_color('easy')
            self.ids.medium_btn.btn_color = self.get_diff_color('medium')
            self.ids.hard_btn.btn_color = self.get_diff_color('hard')
            self.ids.slow_btn.btn_color = self.get_speed_color('slow')
            self.ids.normal_btn.btn_color = self.get_speed_color('normal')
            self.ids.fast_btn.btn_color = self.get_speed_color('fast')
            self.ids.pts5_btn.btn_color = self.get_points_color(5)
            self.ids.pts10_btn.btn_color = self.get_points_color(10)
            self.ids.pts15_btn.btn_color = self.get_points_color(15)
            self.ids.pts20_btn.btn_color = self.get_points_color(20)
            self.ids.paddle_small.btn_color = self.get_paddle_color('small')
            self.ids.paddle_normal.btn_color = self.get_paddle_color('normal')
            self.ids.paddle_large.btn_color = self.get_paddle_color('large')
        except Exception:
            pass
    
    def set_difficulty(self, level):
        GameSettings.difficulty = level
        self.update_buttons()
        
    def set_speed(self, speed):
        GameSettings.ball_speed = speed
        self.update_buttons()
        
    def set_ball_color(self, color):
        GameSettings.ball_color = color
        
    def set_win_points(self, points):
        GameSettings.win_points = points
        self.update_buttons()
    
    def set_paddle_size(self, size):
        GameSettings.paddle_size = size
        self.update_buttons()
        
    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'menu'


class InfoScreen(Screen):
    """Экран информации"""
    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'menu'


class WinScreen(Screen):
    """Экран победы/поражения"""
    def set_winner(self, player_won, robot_score, player_score):
        if player_won:
            self.ids.win_title.text = "ПОБЕДА!"
            self.ids.win_title.color = (0.3, 1, 0.5, 1)
        else:
            self.ids.win_title.text = "ПОРАЖЕНИЕ"
            self.ids.win_title.color = (1, 0.35, 0.35, 1)
        self.ids.win_score.text = f"Робот {robot_score} : {player_score} Игрок"
    
    def play_again(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'game'
        Clock.schedule_once(lambda dt: self.manager.get_screen('game').ids.pong_game.reset_game(), 0.1)
        
    def go_to_menu(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'menu'


class ScorePanel(Widget):
    """Панель счёта"""
    score = NumericProperty(0)
    title = StringProperty("ИГРОК")
    bg_color = ListProperty([0.2, 0.5, 0.3, 0.92])
    title_color = ListProperty([1, 1, 1, 1])
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (dp(110), dp(62))
        self.bind(pos=self.redraw, size=self.redraw, score=self.redraw)
        Clock.schedule_once(lambda dt: self.redraw(), 0)
        
    def redraw(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(0, 0, 0, 0.4)
            RoundedRectangle(
                pos=(self.x + dp(3), self.y - dp(3)),
                size=self.size,
                radius=[dp(12)]
            )
            Color(*self.bg_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(12)])
            Color(1, 1, 1, 0.08)
            RoundedRectangle(
                pos=(self.x + dp(2), self.y + self.height * 0.5),
                size=(self.width - dp(4), self.height * 0.45),
                radius=[dp(10), dp(10), 0, 0]
            )
        
        self.clear_widgets()
        
        title_label = Label(
            text=self.title,
            font_size=sp(10),
            bold=True,
            color=self.title_color,
            size_hint=(None, None),
            size=(self.width, dp(16)),
            pos=(self.x, self.top - dp(18))
        )
        
        score_label = Label(
            text=str(self.score),
            font_size=sp(28),
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(self.width, dp(38)),
            pos=(self.x, self.y + dp(2))
        )
        
        self.add_widget(title_label)
        self.add_widget(score_label)


class Paddle(Widget):
    """Ракетка"""
    color = ListProperty([0.4, 0.85, 1, 1])
    glow_color = ListProperty([0.4, 0.85, 1, 0.3])
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (dp(12), GameSettings.get_paddle_height())
        self.bind(pos=self.redraw, size=self.redraw)
    
    def update_size(self):
        self.height = GameSettings.get_paddle_height()
        self.redraw()
    
    def redraw(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(*self.glow_color)
            RoundedRectangle(
                pos=(self.x - dp(4), self.y - dp(4)),
                size=(self.width + dp(8), self.height + dp(8)),
                radius=[dp(8)]
            )
            Color(0, 0, 0, 0.35)
            RoundedRectangle(
                pos=(self.x + dp(2), self.y - dp(2)),
                size=self.size,
                radius=[dp(5)]
            )
            Color(*self.color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(5)])
            Color(1, 1, 1, 0.25)
            RoundedRectangle(
                pos=(self.x + dp(2), self.y + self.height * 0.55),
                size=(self.width - dp(4), self.height * 0.4),
                radius=[dp(4), dp(4), 0, 0]
            )


class Ball(Widget):
    """Мяч с эффектами"""
    vx = NumericProperty(0)
    vy = NumericProperty(0)
    velocity = ReferenceListProperty(vx, vy)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (dp(18), dp(18))
        self.trail = []
        self.bind(pos=self.redraw)
    
    def redraw(self, *args):
        self.canvas.clear()
        clr = GameSettings.get_ball_rgba()
        
        with self.canvas:
            trail_len = len(self.trail)
            for i, pos in enumerate(self.trail[-8:]):
                alpha = (i + 1) / 12 * 0.5
                size_mult = 0.3 + (i / max(trail_len, 1)) * 0.5
                Color(clr[0], clr[1], clr[2], alpha)
                s = self.width * size_mult
                Ellipse(
                    pos=(pos[0] + (self.width - s) / 2, pos[1] + (self.height - s) / 2),
                    size=(s, s)
                )
            
            Color(clr[0], clr[1], clr[2], 0.2)
            Ellipse(
                pos=(self.x - dp(6), self.y - dp(6)),
                size=(self.width + dp(12), self.height + dp(12))
            )
            
            Color(clr[0], clr[1], clr[2], 0.35)
            Ellipse(
                pos=(self.x - dp(3), self.y - dp(3)),
                size=(self.width + dp(6), self.height + dp(6))
            )
            
            Color(*clr)
            Ellipse(pos=self.pos, size=self.size)
            
            Color(1, 1, 1, 0.45)
            Ellipse(
                pos=(self.x + self.width * 0.25, self.y + self.height * 0.5),
                size=(self.width * 0.3, self.height * 0.25)
            )
    
    def move(self):
        self.trail.append((self.x, self.y))
        if len(self.trail) > 10:
            self.trail.pop(0)
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    """Основная игра"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.ball = Ball()
        self.robot_paddle = Paddle()
        self.player_paddle = Paddle()
        
        self.robot_paddle.color = [1, 0.35, 0.4, 1]
        self.robot_paddle.glow_color = [1, 0.35, 0.4, 0.25]
        self.player_paddle.color = [0.35, 1, 0.5, 1]
        self.player_paddle.glow_color = [0.35, 1, 0.5, 0.25]
        
        self.robot_panel = ScorePanel()
        self.robot_panel.title = "РОБОТ"
        self.robot_panel.bg_color = [0.55, 0.1, 0.12, 0.92]
        self.robot_panel.title_color = [1, 0.75, 0.75, 1]
        
        self.player_panel = ScorePanel()
        self.player_panel.title = "ИГРОК"
        self.player_panel.bg_color = [0.08, 0.42, 0.18, 0.92]
        self.player_panel.title_color = [0.75, 1, 0.82, 1]
        
        self.pause_btn = Button(
            text="||",
            font_size=sp(18),
            bold=True,
            size_hint=(None, None),
            size=(dp(48), dp(36)),
            background_color=(0, 0, 0, 0),
            background_normal='',
            color=(1, 1, 1, 0.95)
        )
        self.pause_btn.bind(on_release=lambda x: self.pause())
        
        for widget in [self.ball, self.robot_paddle, self.player_paddle, 
                       self.robot_panel, self.player_panel, self.pause_btn]:
            self.add_widget(widget)
        
        self.paused = True
        self.game_loop = None
        self.robot_score = 0
        self.player_score = 0
        
        self.bind(size=self.on_resize, pos=self.on_resize)
    
    def on_resize(self, *args):
        """Обновление позиций при изменении размера"""
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.015, 0.015, 0.05, 1)
            Rectangle(pos=self.pos, size=self.size)
            
            Color(0.1, 0.2, 0.4, 0.12)
            Ellipse(
                pos=(self.width * 0.6, -self.height * 0.2),
                size=(self.width * 0.5, self.width * 0.5)
            )
            Color(0.3, 0.1, 0.3, 0.08)
            Ellipse(
                pos=(-self.width * 0.1, self.height * 0.5),
                size=(self.width * 0.4, self.width * 0.4)
            )
            
            Color(0.3, 0.5, 0.8, 0.25)
            Line(
                points=[self.center_x, self.y + dp(10), self.center_x, self.top - dp(10)],
                width=dp(2),
                dash_length=dp(15),
                dash_offset=dp(8)
            )
            
            Color(0.3, 0.5, 0.8, 0.12)
            Line(
                circle=(self.center_x, self.center_y, min(self.width, self.height) * 0.12),
                width=dp(2)
            )
        
        self.robot_panel.pos = (dp(10), self.height - self.robot_panel.height - dp(8))
        self.player_panel.pos = (self.width - self.player_panel.width - dp(10), 
                                  self.height - self.player_panel.height - dp(8))
        
        self.pause_btn.pos = (self.center_x - self.pause_btn.width / 2, 
                              self.height - self.pause_btn.height - dp(12))
        
        self.pause_btn.canvas.before.clear()
        with self.pause_btn.canvas.before:
            Color(0.18, 0.18, 0.3, 0.9)
            RoundedRectangle(pos=self.pause_btn.pos, size=self.pause_btn.size, radius=[dp(10)])
        
        self.robot_paddle.x = dp(15)
        self.player_paddle.x = self.width - self.player_paddle.width - dp(15)
    
    def reset_game(self):
        """Сброс игры"""
        self.robot_score = 0
        self.player_score = 0
        self.paused = False
        
        self.robot_panel.score = 0
        self.player_panel.score = 0
        
        self.robot_paddle.update_size()
        self.player_paddle.update_size()
        
        self.on_resize()
        
        self.robot_paddle.center_y = self.center_y
        self.player_paddle.center_y = self.center_y
        
        if self.game_loop:
            self.game_loop.cancel()
        
        Clock.schedule_once(lambda dt: self.serve(), 0.3)
        self.game_loop = Clock.schedule_interval(self.tick, 1/60.0)
    
    def serve(self):
        """Подача мяча"""
        self.ball.center = self.center
        self.ball.trail = []
        
        direction = 1 if randint(0, 1) == 0 else -1
        speed = GameSettings.get_ball_speed()
        angle = randint(-35, 35)
        
        self.ball.velocity = Vector(speed * direction, 0).rotate(angle)
    
    def tick(self, dt):
        """Игровой цикл"""
        if self.paused:
            return
        
        self.ball.move()
        self.ball.redraw()
        self.ai_move()
        self.clamp_paddles()
        self.check_collisions()
        self.check_goals()
    
    def ai_move(self):
        """Движение ИИ"""
        ai_speed = GameSettings.get_ai_speed()
        
        if self.ball.vx < 0:
            target = self.ball.center_y
            
            if GameSettings.difficulty == 'easy':
                target += randint(-40, 40)
            elif GameSettings.difficulty == 'medium':
                target += randint(-15, 15)
            
            diff = target - self.robot_paddle.center_y
            
            if abs(diff) > dp(5):
                move = min(ai_speed, abs(diff) * 0.18)
                self.robot_paddle.center_y += move if diff > 0 else -move
        
        self.robot_paddle.redraw()
        self.player_paddle.redraw()
    
    def clamp_paddles(self):
        """Ограничение движения ракеток"""
        for paddle in [self.robot_paddle, self.player_paddle]:
            if paddle.y < 0:
                paddle.y = 0
            elif paddle.top > self.height:
                paddle.top = self.height
    
    def check_collisions(self):
        """Проверка столкновений"""
        ball = self.ball
        
        if ball.y <= 0:
            ball.y = 0
            ball.vy = abs(ball.vy)
        elif ball.top >= self.height:
            ball.top = self.height
            ball.vy = -abs(ball.vy)
        
        for paddle in [self.robot_paddle, self.player_paddle]:
            if paddle.collide_widget(ball):
                offset = (ball.center_y - paddle.center_y) / (paddle.height / 2)
                speed = min(Vector(*ball.velocity).length() * 1.03, 25)
                
                if paddle == self.robot_paddle:
                    angle = offset * 45
                    ball.x = paddle.right + dp(2)
                else:
                    angle = 180 - offset * 45
                    ball.x = paddle.x - ball.width - dp(2)
                
                ball.velocity = Vector(speed, 0).rotate(angle)
    
    def check_goals(self):
        """Проверка голов"""
        if self.ball.right < 0:
            self.player_score += 1
            self.player_panel.score = self.player_score
            if not self.check_win():
                self.serve()
                
        elif self.ball.x > self.width:
            self.robot_score += 1
            self.robot_panel.score = self.robot_score
            if not self.check_win():
                self.serve()
    
    def check_win(self):
        """Проверка победы"""
        win_pts = GameSettings.win_points
        
        if self.player_score >= win_pts or self.robot_score >= win_pts:
            self.paused = True
            
            if self.game_loop:
                self.game_loop.cancel()
                self.game_loop = None
            
            app = App.get_running_app()
            win_screen = app.root.get_screen('win')
            win_screen.set_winner(
                self.player_score >= win_pts,
                self.robot_score,
                self.player_score
            )
            
            app.root.transition = SlideTransition(direction='left')
            app.root.current = 'win'
            return True
        
        return False
    
    def on_touch_down(self, touch):
        """Обработка касания"""
        if self.pause_btn.collide_point(*touch.pos):
            return super().on_touch_down(touch)
        
        if touch.x > self.width / 2 and not self.paused:
            self.player_paddle.center_y = touch.y
        
        return True
    
    def on_touch_move(self, touch):
        """Обработка движения касания"""
        if touch.x > self.width / 2 and not self.paused:
            self.player_paddle.center_y = touch.y
        
        return True
    
    def pause(self):
        """Пауза игры"""
        if not self.paused:
            self.paused = True
            PausePopup(game=self).open()
    
    def resume_game(self):
        """Продолжить игру"""
        self.paused = False
    
    def go_to_menu(self):
        """Переход в меню"""
        self.paused = True
        
        if self.game_loop:
            self.game_loop.cancel()
            self.game_loop = None
        
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='right')
        app.root.current = 'menu'


class GameScreen(Screen):
    """Экран игры"""
    pass


class PongApp(App):
    """Главное приложение"""
    
    def build(self):
        sm = ScreenManager()
        
        screens = [
            ('menu', MenuScreen),
            ('settings', SettingsScreen),
            ('info', InfoScreen),
            ('game', GameScreen),
            ('win', WinScreen)
        ]
        
        for name, screen_class in screens:
            sm.add_widget(screen_class(name=name))
        
        return sm


if __name__ == '__main__':
    PongApp().run()
