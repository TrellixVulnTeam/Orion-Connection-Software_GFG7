import socket

from src import Constants
from src.networking import NetworkPackets
from src.utils.Logger import utilLogger


class Client:
    """
    The Client class that
    """

    def __init__(self, host: str, address: tuple):
        self.client_sock = socket.socket()

        self.address = address
        self.host_name = host
        self.crypto = None

    def connect(self):
        """
        :return: The connection Validation.
        """
        val = self.client_sock.connect_ex(self.address)
        Constants.Network.IS_ONLINE = val == 0
        return Constants.Network.IS_ONLINE

    def send(self, msg: str) -> bool:
        """
        :param msg: The protocol based msg.
        """
        try:
            if self.crypto is not None:
                size = str(len(msg) * 4).zfill(NetworkPackets.HEADER)
                self.client_sock.send(bytes(size.encode("utf-8")))
                msg = self.crypto.encrypt_message(msg)
                self.client_sock.send(msg.encode('UTF-16LE'))
            else:
                size = str(len(msg)).zfill(NetworkPackets.HEADER)
                self.client_sock.send(bytes(size.encode("utf-8")))
                self.client_sock.send(msg.encode("utf-8"))

            return True

        except Exception as e:
            return False

    def receive(self) -> str or None:
        """
        :return: The raw decoded msg from the network.
        """
        try:
            size = int(str(self.client_sock.recv(NetworkPackets.HEADER).decode("utf-8", "ignore")))
            msg = self.client_sock.recv(size + 1)
            if self.crypto is not None:
                msg = self.crypto.decrypt_message(msg.decode('UTF-16LE'))
            else:
                msg = msg.decode("utf-8", "ignore")
            return msg

        except Exception as e:
            return None
