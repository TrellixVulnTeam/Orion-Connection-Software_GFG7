import socket

from src.Networking import NetMsgBuild, Maneger
from src.ui.UIHandler import OrionServer
from src.utils import Constants
from src.utils.Constants import Network
from src.utils.Logger import Logger


class Server:
    def __init__(self, logger):
        self.comm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.comm_socket.bind(('', Network.COMM_PORT))
        self.comm_socket.listen(1)

        self.broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.log = logger

    def accept(self):
        sock, address = self.s_s.accept()
        pass

    def handle_client(self, sock, address):
        pass

    def run(self):
        pass


if __name__ == '__main__':
    debug_log = Logger('debug', is_console=True)
    server = Server(debug_log)
    Maneger.__init__(server.s_s, debug_log)
    gui = OrionServer(Constants.GUIFiles(debug_log))
    gui.run()

