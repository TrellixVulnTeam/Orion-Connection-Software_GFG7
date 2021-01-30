import wmi
import math


class Computer:
    def __init__(self):
        self.computer = wmi.WMI()
        self.computer_info = self.computer.Win32_ComputerSystem()[0]
        self.os_info = self.computer.Win32_OperatingSystem()[0]
        self.proc_info = self.computer.Win32_Processor()[0]
        self.gpus_info = self.computer.Win32_VideoController()
    
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

    def get_gpu_temps(self):
        pass

    def get_cpu_temps(self):
        pass

    def get_as_str_arr(self):
        return ["SPECS", self.get_os_name(), self.get_ram(), self.get_cpu(), self.get_gpu()]
