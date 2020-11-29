from pathlib import Path
import os


def file_name(name, format='.png', path=str(str(Path.cwd() / 'res' / 'des'))):
    f = name + format
    return os.path.join(path, f)


class GUIFiles:
    def __init__(self):
        self.KV_DES_FILE = file_name("orion_server", format='.kv', path=str(Path.cwd() / 'res'))
        self.DEF_FONT = file_name("Orion", format='.ttf', path=str(Path.cwd() / 'res'))

        self.MAIN_SCREEN = file_name("Main")
        self.ABOUT_SCREEN = file_name("AboutScreen")
        self.CONNECT_SCREEN = file_name("ConnectScreen")
        self.LOGGER_SCREEN = file_name("LoggerScreen")
        self.ABOUT = file_name("About")
        self.CONNECT = file_name("Connect")
        self.LOGGER = file_name("Logger")
        self.BACK_BTN = file_name("BackBTN")

        self.files = [a for a in dir(self) if not a.startswith('__')]
        self.is_load = True
        for file in self.files:
            f = None
            try:
                f = open(file)

            except FileNotFoundError:
                self.is_load = False

            if self.is_load:
                f.close()
