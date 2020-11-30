from src.utils.Constants import Network
from src.networking import NetMsgBuild
from src.networking.Operations import Operations
import socket


def __init__(socket_comm,  logger):
    global sock_comm
    sock_comm = socket_comm
    global log
    log = logger
    NetMsgBuild.__init__(sock_comm, log)


def act():
    pass
