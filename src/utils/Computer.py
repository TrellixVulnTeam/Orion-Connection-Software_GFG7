import math

import psutil
import wmi


class Computer:
    def __init__(self):
        self.computer_psutil = psutil
        self.computer_wmi = wmi.WMI()

        self.computer_info = self.computer_wmi.Win32_ComputerSystem()[0]
        self.os_info = self.computer_wmi.Win32_OperatingSystem()[0]
        self.proc_info = self.computer_wmi.Win32_Processor()[0]
        self.gpus_info = self.computer_wmi.Win32_VideoController()

    def get_os_name(self) -> str:
        return self.os_info.Name.encode('utf-8').split(b'|')[0].decode().replace("Microsoft ", "")

    def get_os_version(self) -> str:
        return ' '.join([self.os_info.Version, self.os_info.BuildNumber])

    def get_ram(self) -> str:
        return str(math.ceil(float(self.os_info.TotalVisibleMemorySize) / 1048576))

    def get_cpu(self) -> str:
        return self.proc_info.Name.replace(" CPU @ ", " - ")

    def get_gpu(self) -> str:
        return self.gpus_info[0].Name if len(self.gpus_info) < 2 else self.gpus_info[1].Name

    def get_specs_as_str_arr(self):
        return ["SPECS", self.get_os_name(), self.get_ram(), self.get_cpu(), self.get_gpu()]

    def get_cpu_usage(self):
        return str(math.ceil(self.computer_psutil.cpu_percent()))

    def get_ram_usage(self):
        return str(math.ceil(self.computer_psutil.virtual_memory().percent))

    def get_use_as_str_arr(self):
        return ["USE", self.get_cpu_usage(), self.get_ram_usage()]
