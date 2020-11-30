SEPARATOR_CHAR = '!'
HEADER = 4


def __init__(socket, logger):
    global sock
    sock = socket
    global log
    log = logger


def assemble(*req):
    final_req = ''
    for request in req:
        final_req += "{}{}".format(request, SEPARATOR_CHAR)

    return final_req


def split(req):
    return req[:len(req) - len(SEPARATOR_CHAR)].split(SEPARATOR_CHAR)


def send(req):
    size = str(len(req)).zfill(HEADER)
    sock.send(bytes(size.encode()))
    sock.send(req.encode())
    log.write("sending {}".format(req))


def recv():
    size = int(str(sock.recv(HEADER).decode()))
    req = sock.recv(size + 1)
    req = req.decode()
    log.write("recv {}".format(req))
    return req
