import random
from Practice2.gpu import GPU
from Practice2.gpu_specification import nvidia, amd, nvidia_chips, amd_chips


class Generator:
    def __create_manufacture(self) -> str:
        self.manufacture = random.choice(["Nvidia", "AMD"])
        return self.manufacture

    def __create_series(self) -> int:
        if self.manufacture == "Nvidia":
            self.series = random.choice(random.choice([i for i in nvidia.keys()]))
        else:
            self.series = random.choice(random.choice([i for i in amd.keys()]))
        return self.series

    def __create_chip(self) -> str:
        if self.manufacture == "Nvidia":
            self.chip = nvidia_chips[self.series]
            if len(self.chip) > 1:
                self.chip = self.chip[random.randint(0, 1)].split()
            elif len(self.chip) == 1:
                self.chip.append("".join(self.chip))
        else:
            self.chip = amd_chips[self.series]
        return str("".join(self.chip))

    def __memory_and_modification(self) -> list:
        if self.manufacture == "Nvidia":
            if self.series == 1030:
                self.memory = 2
                self.mod = ""
                self.frequency = 1227.0
                self.prefix = "GT"
            elif self.series == 1050:
                self.memory = random.randint(2, 4)
                if self.memory == 4:
                    self.mod = "Ti"
                    self.frequency = 1290.0
                elif self.memory == 3:
                    self.mod = ""
                    self.frequency = 1392.0
                else:
                    self.mod = ""
                    self.frequency = 1354.0
                self.prefix = "GTX"
            elif self.series == 1060:
                self.memory = random.choice([3, 6])
                if self.memory == 6:
                    self.frequency = 1506.0
                    self.mod = ""
                else:
                    self.frequency = 1506.0
                    self.mod = ""
                self.prefix = "GTX"
            elif self.series == 1070:
                self.memory = 8
                self.mod = random.choice(["", "Ti"])
                if self.mod == "Ti":
                    self.frequency = 1607.0
                else:
                    self.frequency = 1503.0
                self.prefix = "GTX"
            elif self.series == 1080:
                self.memory = random.choice([8, 11])
                if self.memory == 11:
                    self.mod = "Ti"
                    self.frequency = 1480.0
                else:
                    self.mod = ""
                    self.frequency = 1607.0
                self.prefix = "GTX"
            elif self.series == 1650:
                self.memory = 4
                self.mod = random.choice(["", "Super"])
                if self.mod == "Super":
                    self.frequency = 1530.0
                else:
                    self.frequency = 1485.0
                self.prefix = "GTX"
            elif self.series == 1660:
                self.memory = 6
                self.mod = random.choice(["", "Ti", "Super"])
                if self.mod == "Ti":
                    self.frequency = 1500.0
                elif self.mod == "Super":
                    self.frequency = 1530.0
                else:
                    self.frequency = 1530.0
                self.prefix = "GTX"
            elif self.series == 2060:
                self.memory = random.choice([6, 8])
                if self.memory == 8:
                    self.mod = "Super"
                    self.frequency = 1470.0
                else:
                    self.mod = ""
                    self.frequency = 1365.0
                self.prefix = "RTX"
            elif self.series == 2070:
                self.memory = 8
                self.mod = random.choice(["", "Super"])
                if self.mod == "Super":
                    self.frequency = 1605.0
                else:
                    self.frequency = 1410.0
                self.prefix = "RTX"
            elif self.series == 2080:
                self.memory = random.choice([8, 11])
                if self.memory == 11:
                    self.mod = "Ti"
                    self.frequency = 1350.0
                else:
                    self.mod = random.choice(["", "Super"])
                    if self.mod == "Super":
                        self.frequency = 1650.0
                    else:
                        self.frequency = 1515.0
                self.prefix = "RTX"
            elif self.series == 3050:
                self.memory = 8
                self.mod = ""
                self.frequency = 1552.0
            elif self.series == 3060:
                self.memory = random.choice([8, 12])
                if self.memory == 8:
                    self.mod = "Ti"
                    self.frequency = 1410.0
                else:
                    self.mod = ""
                    self.frequency = 1322.0
                self.prefix = "RTX"
            elif self.series == 3070:
                self.memory = 8
                self.mod = random.choice(["", "Ti"])
                if self.mod == "Ti":
                    self.frequency = 1575.0
                else:
                    self.frequency = 1500.0
                self.prefix = "RTX"
            elif self.series == 3080:
                self.memory = random.choice([10, 12])
                if self.memory == 12:
                    self.mod = random.choice(["", "Ti"])
                    if self.mod == "Ti":
                        self.frequency = 1365.0
                    else:
                        self.frequency = 1260.0
                else:
                    self.mod = ""
                    self.frequency = 1440.0
                self.prefix = "RTX"
            elif self.series == 3090:
                self.memory = 24
                self.mod = random.choice(["", "Ti"])
                if self.mod == "Ti":
                    self.frequency = 1560.0
                else:
                    self.frequency = 1395.0
                self.prefix = "RTX"
            else:
                self.mod, self.memory, self.frequency = "ERROR", 0, 0.0
        else:
            if self.series == 460:
                self.memory = random.choice([2, 4])
                self.mod = ""
                self.frequency = 1090.0
                self.prefix = "RX"
            elif self.series == 470:
                self.memory = random.choice([4, 8])
                self.mod = ""
                self.frequency = 968.0
                self.prefix = "RX"
            elif self.series == 480:
                self.memory = random.choice([4, 8])
                self.mod = ""
                self.frequency = 1120.0
                self.prefix = "RX"
            elif self.series == 550:
                self.memory = 2
                self.mod = ""
                self.frequency = 1100.0
                self.prefix = "RX"
            elif self.series == 560:
                self.memory = random.choice([2, 4])
                self.mod = ""
                self.frequency = 1175.0
                self.prefix = "RX"
            elif self.series == 570:
                self.memory = random.choice([4, 8])
                self.mod = ""
                self.frequency = 1168.0
                self.prefix = "RX"
            elif self.series == 580:
                self.memory = random.choice([4, 8])
                self.mod = ""
                self.frequency = 1257.0
                self.prefix = "RX"
            elif self.series == 590:
                self.memory = 8
                self.mod = ""
                self.frequency = 1469.0
                self.prefix = "RX"
            elif self.series == 5500:
                self.memory = 8
                self.mod = "XT"
                self.frequency = 1670.0
                self.prefix = "RX"
            elif self.series == 5600:
                self.memory = 6
                self.mod = "XT"
                self.frequency = 1130.0
                self.prefix = "RX"
            elif self.series == 5700:
                self.memory = 8
                self.mod = random.choice(["", "XT"])
                if self.mod == "XT":
                    self.frequency = 1605.0
                else:
                    self.frequency = 1465.0
                self.prefix = "RX"
            elif self.series == 6600:
                self.memory = 8
                self.mod = random.choice(["", "XT"])
                if self.mod == "XT":
                    self.frequency = 1968.0
                else:
                    self.frequency = 1626.0
                self.prefix = "RX"
            elif self.series == 6700:
                self.memory = 12
                self.mod = "XT"
                self.frequency = 2321.0
                self.prefix = "RX"
            elif self.series == 6800:
                self.memory = 16
                self.mod = random.choice(["", "XT"])
                if self.mod == "XT":
                    self.frequency = 1825.0
                else:
                    self.frequency = 1700.0
                self.prefix = "RX"
            elif self.series == 6900:
                self.memory = 16
                self.mod = "XT"
                self.frequency = 1825.0
                self.prefix = "RX"
            else:
                self.mod, self.memory, self.frequency = "ERROR", 0, 0.0
        return [self.mod, self.memory, self.frequency, self.prefix]

    def generator(self) -> GPU:
        return GPU(self.__create_manufacture(), self.__create_series(), self.__create_chip(),
                   self.__memory_and_modification(), "7680×4320")

    def generate_1000(self) -> list:
        return [self.generator() for i in range(1000)]

    def generate_10000(self) -> list:
        return [self.generator() for i in range(10000)]


if __name__ == "__main__":
    gen = Generator()
    [print(i) for i in gen.generate_10000()]
