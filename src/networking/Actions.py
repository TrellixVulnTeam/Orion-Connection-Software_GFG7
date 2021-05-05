import ctypes
import os
import webbrowser

from pynput.keyboard import Key, Controller

from src.utils.Computer import Computer
from src.utils.Logger import appLogger

DEF_TIME = 5
MSG = "By the command of Orion Connection"
keyboard_sim = Controller()
MAGIC_FILE = ""
COMPUTER = Computer()


def __sim_keyboard_press__(key, keyboard=keyboard_sim):
    keyboard.press(key)
    keyboard.release(key)


def shut_down():
    command = r'shutdown /s /t 10 /c By_The_Command_Of_Orion_Connection'
    os.system(command)
    appLogger.write("Shut Down")


def restart():
    command = r'shutdown /r /t 10 /c By_The_Command_Of_Orion_Connection'
    os.system(command)
    appLogger.write("Restart")


def log_out():
    os.system(r'shutdown /l')
    appLogger.write("Log Out")


def lock():
    ctypes.windll.user32.LockWorkStation()
    appLogger.write("Lock")


def play_pause():
    __sim_keyboard_press__(Key.media_play_pause)
    appLogger.write("Play Pause Toggle")


def prev_song():
    __sim_keyboard_press__(Key.media_previous)
    appLogger.write("Previous Song")


def next_song():
    __sim_keyboard_press__(Key.media_next)
    appLogger.write("Next Song")


def vol_up():
    __sim_keyboard_press__(Key.media_volume_up)
    appLogger.write("Sound Vol Up")


def vol_down():
    __sim_keyboard_press__(Key.media_volume_down)
    appLogger.write("Sound Vol Down")


def mute():
    __sim_keyboard_press__(Key.media_volume_mute)


def sleep():
    pass


def run_file():
    if "http" in MAGIC_FILE:
        webbrowser.open(MAGIC_FILE)

    elif ".py" in MAGIC_FILE:
        exec(open(MAGIC_FILE).read())

    elif ".exe" in MAGIC_FILE:
        os.system(MAGIC_FILE)



