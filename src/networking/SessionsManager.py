import os
import socket
from random import randint

from src import Constants
from src.Constants import Network
from src.networking import NetworkPackets, Actions
from src.networking.Client import Client
from src.utils.DH_Encryption import Encryption
from src.utils.Enum import Enum


class SessionManager:
    """
    This class is responsible for dealing with any flow of net msgs.
    """

    def __init__(self):
        address = (Network.SERVER_IP, Network.SERVER_PORT)
        self.client = Client(str(socket.gethostname()), address)
        self.val = self.client.connect()
        if not self.val:
            Network.IS_ONLINE = False

    def go_crypto(self):
        msg = NetworkPackets.split(self.client.receive())
        g = int(msg[1])
        n = int(msg[2])
        g_pow_a_mod_n = int(msg[3])
        crypto = Encryption(g, n)
        crypto.get_full_key(g_pow_a_mod_n)
        self.client.send(NetworkPackets.assemble(NetworkPackets.NetLogicIncomes.CONNECT.value,
                                                 str(crypto.get_partial_key())))
        self.client.crypto = crypto

    def gen_id(self) -> str:
        num = str(randint(1, 9999))
        num = num.zfill(4)
        return num

    def open_id_file(self):
        try:
            open(Constants.Files.ID, 'r+').close()
        except FileNotFoundError:
            open(Constants.Files.ID, 'x').close()
        finally:
            file = open(Constants.Files.ID, 'r+')
            return file

    def sync(self):
        """
        This function contains the full process of the sync phase.
        """
        if Network.IS_ONLINE:
            self.go_crypto()
            num = ""
            file = self.open_id_file()

            if os.path.getsize(Constants.Files.ID) == 0:  # Empty
                is_valid = False
                while not is_valid:
                    num = self.gen_id()
                    self.client.send(NetworkPackets.assemble("COMPUTER", "ID_VAL", num))
                    msg = NetworkPackets.split(self.client.receive())
                    is_valid = msg[0] == NetworkPackets.NetLogicIncomes.VALID.value

                file.write(num)

            else:
                is_valid = False
                num = file.read()
                while not is_valid:
                    self.client.send(NetworkPackets.assemble("COMPUTER", "ID_VAL", num))
                    msg = NetworkPackets.split(self.client.receive())
                    is_valid = msg[0] == NetworkPackets.NetLogicIncomes.VALID.value
                    if not is_valid:
                        num = self.gen_id()

                if num != file.read():
                    file.close()
                    os.remove(Constants.Files.ID)
                    file = self.open_id_file()
                    file.write(num)

            file.close()

    def manage(self, incoming: str):
        """
        This functions deals with the execution of the required operations.
        :param incoming: Raw net msg.
        """
        if Network.IS_ONLINE:
            incoming = NetworkPackets.split(incoming)[0]
            if incoming in Operation.list():

                if incoming == Operation.VOL_UP.value:
                    Actions.vol_up()
                elif incoming == Operation.VOL_DOWN.value:
                    Actions.vol_down()
                elif incoming == Operation.PAUSE_PLAY_TOGGLE.value:
                    Actions.play_pause()
                elif incoming == Operation.SKIP.value:
                    Actions.next_song()
                elif incoming == Operation.PREV.value:
                    Actions.prev_song()
                elif incoming == Operation.MUTE.value:
                    Actions.mute()
                elif incoming == Operation.OFF.value:
                    Actions.shut_down()
                elif incoming == Operation.SLEEP.value:
                    Actions.sleep()
                elif incoming == Operation.RESTART.value:
                    Actions.restart()
                elif incoming == Operation.LOCK.value:
                    Actions.lock()
                elif incoming == Operation.LOG_OUT.value:
                    Actions.log_out()
                elif incoming == Operation.MAGIC_BTN.value:
                    Actions.run_file()
                elif incoming == Operation.USAGE.value:
                    self.client.send(NetworkPackets.assemble(arr=Actions.COMPUTER.get_use_as_str_arr()))

                elif incoming == Operation.DISCONNECT.value:
                    self.client.send(NetworkPackets.assemble(Operation.DISCONNECT.value))
                    return Operation.DISCONNECT

            elif incoming in NetworkPackets.NetLogicIncomes.list():
                if incoming == NetworkPackets.NetLogicIncomes.PAIRED.value:
                    Constants.Network.IS_PAIRING = True
                    self.client.send(NetworkPackets.assemble(arr=Actions.COMPUTER.get_specs_as_str_arr()))
                elif incoming == NetworkPackets.NetLogicIncomes.INVALID:
                    pass


class Operation(Enum):
    """
    All the operations that can be asked to execute.
    """
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
    MAGIC_BTN = "MAGIC"
    SPECS_INFO = "SPECS"
    USAGE = "USE"
