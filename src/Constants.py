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

        self.files = [self.MAIN_SCREEN, self.ABOUT_SCREEN, self.CONNECT_SCREEN, self.LOGGER_SCREEN, self.ABOUT,
                      self.LOGGER, self.CONNECT, self.BACK_BTN, self.KV_DES_FILE, self.DEF_FONT]
    #     self.check_files()
    #
    # def check_files(self):
    #     is_load = True
    #     for file in self.files:
    #         f = None
    #         try:
    #             f = open(file)
    #
    #         except FileNotFoundError:
    #             is_load = False
    #             self.log.write("ERROR loading {}".format(file))
    #
    #         if f is not None:
    #             f.close()
    #
    #     if is_load:
    #         self.log.write("Loaded ALL GUI")


class Network:   
    SERVER_PORT = 1690
    SERVER_IP = "127.0.0.1"
