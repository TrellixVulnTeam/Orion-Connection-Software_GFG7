import os
import ctypes
from pynput.keyboard import Key, Controller
import GPUtil
import psutil

from src.utils.Logger import appLogger

DEF_TIME = 15
MSG = "By the command of Orion Connection"
keyboard_sim = Controller()
gpu = GPUtil.getGPUs()[0]


def __sim_keyboard_press__(key, keyboard=keyboard_sim):
    keyboard.press(key)
    keyboard.release(key)


def shut_down(with_timer=True, sec=DEF_TIME, with_msg=True):
    command = r'shutdown /s{}{}'.format(r' /t ' + str(sec) if with_timer else "", r'/c ' + MSG if with_msg else "")
    os.system(command)
    appLogger.write("Shut Down")


def restart(with_timer=True, sec=DEF_TIME, with_msg=True):
    command = r'shutdown /r{}'.format(r' /t ' + str(sec) if with_timer else "", r'/c ' + MSG if with_msg else "")
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


def gpu_name():
    return gpu.name


def gpu_temp():
    return gpu.temperature


def mute():
    pass


def sleep():
    pass
