from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from win32api import GetSystemMetrics

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window

from src import Constants
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


class ConnectPairScreen(Screen):
    pass


class ConnectIDScreen(Screen):
    pass


class ConnectOfflineScreen(Screen):
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


class TransTextInput(TextInput):
    def __init__(self, **kwargs):
        super(TransTextInput, self).__init__(**kwargs)


class IDTextWidget(TransTextInput):
    def __init__(self, **kwargs):
        super(TransTextInput, self).__init__(**kwargs)
        self.text = open(Constants.Files.ID, 'r').read()
        self.cursor_blink = False
        self.font_name = Constants.Files.DEF_FONT
        self.font_size = 140



'''
    App
'''


class OrionServer(App):
    def __init__(self, **kwargs):
        super(OrionServer, self).__init__(**kwargs)
        self.assets = Constants.Files
        self.kv_des = Builder.load_file(self.assets.KV_DES_FILE)

    def build(self):
        self.title = "Orion Server" + chr(169)

        Window.size = (GetSystemMetrics(0), GetSystemMetrics(1))
        Window.fullscreen = False

        return self.kv_des

    def choose_connect_screen(self):
        if not Constants.Network.IS_ONLINE:
            return "ConnectOfflineScreen"
        else:
            if not Constants.Network.IS_PAIRED:
                return "ConnectPairScreen"
            else:
                return "ConnectScreen"

    def update_id(self):
        text_input = self.root.ids.ConnectIDScreen.ids.id_widg
        text_input.text = open(Constants.Files.ID, 'r').read()
