from src import Constants
from src.networking import NetworkPackets
from src.networking.SessionsManager import SessionManager, Operation
from src.ui.UIHandler import OrionServer
import threading
import time
from src.utils.Logger import utilLogger


class OrionSoftware:
    """
    The main class that contains the ui and the network handlers.
    """
    def __init__(self):
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
        while not Constants.Network.IS_ONLINE:
            utilLogger.write("Reconnecting...")
            val = self.network.client.connect()
            if not val:
                time.sleep(7)

        self.network.sync()
        done = False
        while not done:
            try:
                msg = self.network.client.receive()

                if msg is None:
                    raise Exception

                elif msg != "":
                    val = self.network.manage(msg)


            except Exception as e:
                print(e.__traceback__)
                done = True


if __name__ == '__main__':
    software = OrionSoftware()
    print(NetworkPackets.get_mac_add())
    software.start_comm()
    software.start_ui()


