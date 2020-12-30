import socket

from src.networking import NetworkPackets, Actions

from src.networking.Client import Client
from src.Constants import Network
from src.utils.Enum import Enum


class SessionManager:
    def __init__(self):
        address = (Network.SERVER_IP, Network.SERVER_PORT)
        self.client = Client(str(socket.gethostname()), address)
        self.val = self.client.connect()
        if not self.val:
            pass

    def sync(self):
        self.client.send(NetworkPackets.assemble("COMPUTER", "ID_VAL", '3339'))

    def manage(self, incoming: str):
        incoming = NetworkPackets.split(incoming)[0]
        if incoming in Operation.list():

            if incoming == Operation.VOL_UP.value: Actions.vol_up()
            elif incoming == Operation.VOL_DOWN.value: Actions.vol_down()
            elif incoming == Operation.PAUSE_PLAY_TOGGLE.value: Actions.play_pause()
            elif incoming == Operation.SKIP.value: Actions.next_song()
            elif incoming == Operation.PREV.value: Actions.prev_song()
            elif incoming == Operation.MUTE.value: Actions.mute()
            elif incoming == Operation.OFF.value: Actions.shut_down()
            elif incoming == Operation.SLEEP.value: Actions.sleep()
            elif incoming == Operation.RESTART.value: Actions.restart()
            elif incoming == Operation.LOCK.value: Actions.lock()
            elif incoming == Operation.LOG_OUT.value: Actions.log_out()

            elif incoming == Operation.DISCONNECT.value:
                pass

        elif incoming in NetworkPackets.NetLogicIncomes.list():
            if incoming == NetworkPackets.NetLogicIncomes.INVALID:
                pass


class Operation(Enum):
    VOL_UP = "VOL_UP"
    VOL_DOWN = "VOL_DOWN"
    PAUSE_PLAY_TOGGLE = "PTT"
    SKIP = "SKIP"
    PREV = "PREV"
    MUTE = "MUTE"
    OFF = "OFF"
    SLEEP = "SLEEP"
    RESTART = "RESTRT"
    LOCK = "LCK"
    LOG_OUT = "LGOT"
    DISCONNECT = "DISCON"


if __name__ == '__main__':
    SessionManager.manage(NetworkPackets.assemble("PTT"))