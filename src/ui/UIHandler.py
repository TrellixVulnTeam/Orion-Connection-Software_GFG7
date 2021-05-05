import os
import webbrowser

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from win32api import GetSystemMetrics

from src import Constants
from src.networking import NetworkPackets, Actions
from src.ui.ComplexButton import ComplexButton
from src.utils.Logger import appLogger


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


class SettingsScreen(Screen):
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
        self.file = None
        try:
            self.file = open(Constants.Files.ID, 'r')
        except Exception:
            self.file = open(Constants.Files.ID, 'x')
        finally:
            try:
                self.text = self.file.read()
                self.file.close()
            except Exception:
                self.text = ""

        self.cursor_blink = False
        self.font_size = 140
        self.readonly = True
        self.font_name = Constants.Files.DEF_FONT


class MagicPathInput(TextInput):
    def __init__(self, **kwargs):
        super(MagicPathInput, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.foreground_color = (0, 0, 0, 1)
        self.text = "Path"
        self.cursor_blink = True
        self.font_size = 25
        self.cursor_color = (0, 0, 0, 1)
        self.multiline = False


class LogView(ScrollView):
    def __init__(self, **kwargs):
        super(LogView, self).__init__(**kwargs)

        self.bar_width = 30
        self.size_hint = (1, 0.81)
        self.scroll_type = ['bars']
        self.bar_inactive_color = (5, 20, 10, 0.5)
        self.do_scroll_x = False
        self.do_scroll_y = True

        file = open(Constants.Files.LOG, 'r')
        self.text_log = file.read().split('\n')
        file.close()

        self.index = len(self.text_log)

        self.__init__grid()

    def __init__grid(self):
        self.grid = GridLayout()
        self.grid.size_hint_y = None
        self.grid.cols = 1
        self.grid.spacing = 0
        self.grid.padding = (0, -100)
        self.grid.size_hint_x = 1.0
        self.grid.row_default_height = '48dp'
        self.write(self.text_log[:self.index - 1])
        self.add_widget(self.grid)

    def write(self, to_write: list):
        for log in to_write:
            widg = Label(text=log)
            widg.size_hint_y = None
            widg.font_size = 36
            widg.padding = (0, 0)
            widg.height = 50
            widg.valign = 'middle'
            widg.halign = 'left'

            # increment grid height
            self.grid.height += widg.height

            self.grid.add_widget(widg)

    def clean(self):
        appLogger.clean()
        self.grid.clear_widgets()

'''
    App
'''


class OrionServer(App):
    def __init__(self, client, **kwargs):
        super(OrionServer, self).__init__(**kwargs)
        self.assets = Constants.Files
        self.kv_des = Builder.load_file(self.assets.KV_DES_FILE)
        self.client = client
        Clock.schedule_interval(self.paired, 5)
        Clock.schedule_interval(self.update_log, 5)

    def build(self):
        self.title = "Orion Connection" + chr(169)

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

    def paired(self, *args):
        if self.root is not None:
            if self.root.current != "LoggerScreen":
                if Constants.Network.IS_PAIRING:
                    Constants.Network.IS_PAIRED = True
                    Constants.Network.IS_PAIRING = False
                    self.root.current = "ConnectScreen"

    def disconnect(self):
        self.client.send(NetworkPackets.assemble(NetworkPackets.NetCommands.DISCONNECT.value))
        self.root.current = "ConnectPairScreen"
        Constants.Network.IS_PAIRED = False

    def refresh_connection(self):
        if Constants.Network.IS_ONLINE:
            self.root.current = "ConnectPairScreen"

    def update_log(self, *args):
        if self.root is not None:
            if self.root.current == "LoggerScreen":
                file = open(Constants.Files.LOG, 'r')
                text = file.read().split('\n')
                file.close()
                current_index = len(text)
                if current_index > self.root.ids.LoggerScreen.ids.log_view.index:
                    self.root.ids.LoggerScreen.ids.log_view. \
                        write(text[self.root.ids.LoggerScreen.ids.log_view.index - 1:])
                    self.root.ids.LoggerScreen.ids.log_view.index = current_index

    def open_link(self, *args):
        webbrowser.open("https://github.com/OfekHarel?tab=repositories")

    def clean_log(self):
        if self.root is not None:
            self.root.ids.LoggerScreen.ids.log_view.clean()

    def export_log(self):
        appLogger.export()

    def transfer_magic(self):
        if self.root is not None:
            Actions.MAGIC_FILE = self.root.ids.SettingsScreen.ids.magic_file_input.text
