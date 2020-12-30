import socket

from src.networking import NetworkPackets


class Client():
    def __init__(self, host: str, address: tuple):
        self.client_sock = socket.socket()
        self.address = address
        self.host_name = host

    def connect(self):
        """
        :return: The connection Validation.
        """
        valid = True
        try:
            self.client_sock.connect(self.address)

        except:
            valid = False
            print("lol")

        finally:
            return valid

    def send(self, msg: str):
        """
        :param msg: The protocol based msg.
        """
        size = str(len(msg)).zfill(NetworkPackets.HEADER)
        self.client_sock.send(bytes(size.encode()))
        self.client_sock.send(msg.encode())

    def receive(self):
        """
        :return: The raw decoded msg from the network.
        """
        try:
            size = int(str(self.client_sock.recv(NetworkPackets.HEADER).decode()))
            req = self.client_sock.recv(size + 1)
            return req.decode()

        except Exception as e:
            print(e.__traceback__)


