import socket

from src.networking import NetMsgBuild, Maneger
from src.networking.Operations import Operations
from src.ui.UIHandler import OrionServer
from src.utils import Constants
from src.utils.Constants import Network
from src.utils.Logger import Logger


class Server:
    def __init__(self, logger):
        self.comm_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.comm_socket.bind(('', Network.COMM_PORT))
        self.comm_socket.listen(30)

        self.broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        self.log = logger

    def broadcast(self):
        msg = NetMsgBuild.assemble(Operations.BROADCAST.value, socket.gethostbyname(socket.gethostname()),
                                   Network.COMM_PORT, socket.gethostname())
        self.log.write(msg)
        self.broadcast_socket.sendto(msg.encode(), (Network.BROAD_IP, Network.BROAD_PORT))
        sock, address = self.comm_socket.accept()
        self.handle(sock, address)

    def handle(self, sock, address):
        self.log.write("Connected to {}".format(address))
        Maneger.__init__(socket, self.log)

        while True:
            Maneger.act()


if __name__ == '__main__':
    debug_log = Logger('debug', is_console=True)
    server = Server(debug_log)
    server.broadcast()
    gui = OrionServer(Constants.GUIFiles(debug_log))
    gui.run()

