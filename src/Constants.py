import os
from pathlib import Path


def __file_name__(name: str, format='.png', path=str(str(Path.cwd() / 'res' / 'des'))) -> str:
    """
    A util function for helping in the path naming process.
    :param name: The name of the file.
    :param format: The format of the file. Default is PNG
    :param path: The abs path of the file. Default is under .../res/des/
    :return: The full abs path of the file.
    """

    f = name + format
    return os.path.join(path, f)


class Files:
    """
    A const class that contains all the files paths.
    """
    KV_DES_FILE = __file_name__("orion_des", format='.kv', path=str(Path.cwd() / 'res'))
    DEF_FONT = __file_name__("Orion", format='.ttf', path=str(Path.cwd() / 'res'))
    ID = __file_name__("id", format='.txt', path=str(Path.cwd() / 'res'))
    LOG = __file_name__("EventLog", format='.log', path=str(Path.cwd()).replace('src', 'logs'))

    MAIN_SCREEN = __file_name__("Main")
    ABOUT_SCREEN = __file_name__("AboutScreen")
    CONNECT_SCREEN = __file_name__("ConnectScreen")
    LOGGER_SCREEN = __file_name__("LoggerScreen")
    SETTINGS_SCREEN = __file_name__("SettingsScreen")
    ABOUT = __file_name__("About")
    CONNECT = __file_name__("Connect")
    LOGGER = __file_name__("Logger")
    SETTINGS = __file_name__("Settings")
    BACK_BTN = __file_name__("BackBTN")
    ID_FRAME = __file_name__("IDFrame")
    PAIR_IMG = __file_name__("PairIMG")
    PAIR_BTN = __file_name__("PairBTN")
    DISCONNECT_BTN = __file_name__("DisconnectBTN")
    CONNECTED_TITLE = __file_name__("ConnectedTitle")
    OFFLINE_TITLE = __file_name__("OfflineTitle")
    REFRESH_BTN = __file_name__("RefreshBTN")
    EXPORT_LOG = __file_name__("ExportLog")
    CLEAN_LOG = __file_name__("CleanLog")
    MAGIC_PATH_TXT = __file_name__("MagicPath")
    MAGIC_PATH_INPUT = __file_name__("MagicPathInput")


class Network:
    """
    A const class That contains all th network params5000
    """
    SERVER_PORT = 1691
    LOCAL_IP = "127.0.0.1"
    PUBLIC_IP = "192.46.233.145"
    IS_LOCAL = True
    SERVER_IP = LOCAL_IP if IS_LOCAL else PUBLIC_IP
    IS_ONLINE = True
    IS_PAIRED = False
    IS_PAIRING = False
