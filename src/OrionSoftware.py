import threading
import time
import socket


from src import Constants
from src.networking.SessionsManager import SessionManager
from src.ui.UIHandler import OrionServer
from src.utils.Logger import utilLogger


class OrionSoftware:
    """
    The main class that contains the ui and the network handlers.
    """

    def __init__(self):
        utilLogger.clean()
        self.network = SessionManager()
        self.net_thread = None

        self.software_ui = OrionServer(self.network.client)
        self.ui_thread = None

    def start_ui(self):
        """
        Starts a UI thread.
        """
        self.ui_thread = threading.Thread(target=self.software_ui.run())
        utilLogger.write("Exiting UI")
        self.ui_thread.start()

    def start_comm(self):
        """
        Initial communication sync process and starts a network handler thread.
        """
        self.net_thread = threading.Thread(target=self.commun)
        utilLogger.write("Starting Network")
        self.net_thread.start()

    def commun(self):
        """
        The in going communication flow
        """
        while True:
            while not Constants.Network.IS_ONLINE:
                val = self.network.client.connect()
                if not val:
                    utilLogger.write("Reconnecting...")
                    time.sleep(10)

            self.network.sync()
            done = False
            while not done:
                try:
                    msg = self.network.client.receive()

                    if msg is None:
                        done = True

                    elif msg != "":
                        self.network.manage(msg)

                except Exception:
                    done = True

            Constants.Network.IS_ONLINE = False
            self.network.client.client_sock = socket.socket()
            self.network.client.crypto = None


if __name__ == '__main__':
    software = OrionSoftware()
    software.start_comm()
    software.start_ui()
