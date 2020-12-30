import logging
from pathlib import Path
from datetime import datetime
import os


class Logger:
    """
    A custom logger class.
    """
    def __init__(self, log_name: str, is_console=False):
        self.FORMAT = '.log'
        self.log_name = log_name
        self.is_console = is_console
        self.logger = logging.getLogger(self.log_name)
        self.path = os.path.join(str(Path.cwd()).replace('src', 'logs'))

        try:
            os.makedirs(self.path)

        except FileExistsError:
            pass

        self.path = os.path.join(self.path, self.log_name + self.FORMAT)
        self.log = logging.FileHandler(self.path)
        self.log.setLevel(logging.INFO)
        self.logger.addHandler(self.log)

    def write(self, msg: str):
        """
        Writes a msg to the logger.
        :param msg: The msg to write.
        """
        self.logger.error("{} --> {}\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), msg))
        if self.is_console:
            print("[LOG] \033[92m-name={}-\033[1;36m {} \033[;1m".format(self.log_name, msg))

    def read(self) -> str:
        """
        Reads the whole logger.
        :return: The full logger string.
        """
        return open(self.path, 'r').read()

    def export(self, path: str, name='log'):
        """
        This function bring the ability to export the whole log file to other external file.
        :param path: The full abs path to export to.
        :param name: The name of the file. Default as "log"
        """
        name += self.FORMAT
        try:
            os.makedirs(path)

        except FileExistsError:
            pass

        open(os.path.join(path, name), 'w').write("Log Export: {}\n".format(
            datetime.now().strftime("%d/%m/%Y %H:%M:%S") + self.read()))


utilLogger = Logger("General", is_console=True)
appLogger = Logger("EventLog", is_console=True)
