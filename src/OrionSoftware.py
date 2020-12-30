from src.networking.SessionsManager import SessionManager
from src.ui.UIHandler import OrionServer
import threading


class OrionSoftware:
    def __init__(self):
        self.software_ui = OrionServer()
        self.ui_thread = None
        self.network = SessionManager()
        self.net_thread = None

    def start_ui(self):
        self.ui_thread = threading.Thread(target=self.software_ui.run())
        self.ui_thread.start()

    def start_comm(self):
        self.network.sync()
        self.net_thread = threading.Thread(target=self.comm)
        self.net_thread.start()

    def comm(self):
        done = False
        while not done:
            try:
                msg = self.network.client.receive()
                if msg != "":
                    self.network.manage(msg)
            except Exception as e:
                print(e)
                done = True


if __name__ == '__main__':
    software = OrionSoftware()
    software.start_comm()
    software.start_ui()

