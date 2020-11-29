from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from win32api import GetSystemMetrics

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.core.window import Window

from src.ui.ComplexButton import ComplexButton
from src.utils import Constants
from src.utils.StableBoolean import StableBoolean

'''
    Screens
'''


class WindowManager(ScreenManager):
    pass


class MenuScreen(Screen):
    pass


class LoggerScreen(Screen):
    pass


class InfoScreen(Screen):
    pass


'''
    Widgets & Utils
'''


class ImageButton(ComplexButton, Image):
    pass


class TextButton(ComplexButton, Label):
    pass

'''
    App
'''


class OrionServer(App):
    def __init__(self, **kwargs):
        super(OrionServer, self).__init__(**kwargs)
        self.assets = Constants.GUIFiles()
        self.kv_des = Builder.load_file(self.assets.KV_DES_FILE)

    def build(self):
        self.title = "Orion Server" + chr(169)

        Window.size = (GetSystemMetrics(0), GetSystemMetrics(1))
        Window.fullscreen = False

        return self.kv_des


if __name__ == '__main__':
    OrionServer().run()

