from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

from win32api import GetSystemMetrics

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window

from src.ui.ComplexButton import ComplexButton


'''
    Screens
'''


class WindowManager(ScreenManager):
    pass


class MenuScreen(Screen):
    pass


class ConnectScreen(Screen):
    pass


class LoggerScreen(Screen):
    pass


class AboutScreen(Screen):
    pass


'''
    Widgets & Utils
'''


class ImageButton(ComplexButton, Image):
    pass


class TextButton(ComplexButton, Label):
    pass


class BackButton(TextButton):
    pass

'''
    App
'''


class OrionServer(App):
    def __init__(self, const, **kwargs):
        super(OrionServer, self).__init__(**kwargs)
        self.assets = const
        self.kv_des = Builder.load_file(self.assets.KV_DES_FILE)

    def build(self):
        self.title = "Orion Server" + chr(169)

        Window.size = (GetSystemMetrics(0), GetSystemMetrics(1))
        Window.fullscreen = False

        return self.kv_des


