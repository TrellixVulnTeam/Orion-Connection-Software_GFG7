import logging
from pathlib import Path
from datetime import datetime
import os


class Logger:
    def __init__(self, log_name, is_console=False):
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

    def write(self, msg):
        self.logger.error("{} --> {}\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), msg))
        if self.is_console:
            print("[LOG] \033[92m-name={}-\033[1;36m {} \033[;1m".format(self.log_name, msg))

    def read_logger(self):
        return open(self.path, 'r').read()

    def export(self, path, name='log'):
        name += self.FORMAT
        try:
            os.makedirs(path)

        except FileExistsError:
            pass

        open(os.path.join(path, name), 'w').write("Log Export: {}\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                                                                            + self.read_logger()))
