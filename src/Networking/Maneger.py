from src.utils.Constants import Network
from src.Networking import NetMsgBuild
from src.Networking.Operations import Operations


def __init__(socket, logger):
    global sock
    sock = socket
    global log
    log = logger
    NetMsgBuild.__init__(sock, log)


def broadcast():
    msg = NetMsgBuild.assemble(Operations.BROADCAST, sock.gethostbyname(sock.gethostname()), Network.COMM_PORT)
    sock.sendto(msg.encode(), Network.BROAD_PORT)
    


