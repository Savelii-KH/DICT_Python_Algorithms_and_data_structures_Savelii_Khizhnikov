from Practice2.gpu_specification import nvidia, amd


class GPU:
    manufacture: str
    model: int
    chip: str
    mod_memory_frequency: list
    resolution: str
    prefix: str

    def __init__(self, manufacture: str, model: int, chip: str,
                 mod_memory_frequency: list, resolution: str):
        self.manufacture = manufacture
        self.model = model
        self.mod, self.memory, self.frequency, self.prefix = mod_memory_frequency
        self.chip = chip
        self.resolution = resolution

    def __repr__(self) -> str:
        return f"{self.manufacture} {self.prefix} {self.model}{self.mod} {self.memory}GB {self.chip} " \
               f"{self.frequency} MHz {self.resolution}"

    def __eq__(self, other):
        return self.manufacture == other.manufacture and \
               self.model == other.model and \
               self.mod == other.mod and \
               self.memory == other.memory and \
               self.frequency == other.frequency and \
               self.prefix == other.prefix and \
               self.chip == other.chip and \
               self.resolution == other.resolution

    def __print_unknown(self) -> str:
        return f"""Видеокарта: {self.model}{self.mod}
Производитель: {self.manufacture}
Графический чип: {self.chip}
Объем памяти: {self.memory}
Поддерживаемое разрешение экрана {self.resolution}
Отсутствует"""

    def __print_known(self, year) -> str:
        return f"""Видеокарта: {self.prefix} {self.model} {self.mod}
Производитель: {self.manufacture}
Графический чип: {self.chip}
Объем памяти: {self.memory}GB
Частотой ядра: {self.frequency} MHz
Год выпуска: {year}
Поддерживаемое разрешение экрана {self.resolution}
{'-'*40}"""

    def get_info(self) -> str:
        year: int = 0
        if self.manufacture.strip().lower() == "nvidia":
            for i in nvidia:
                if self.model in i:
                    year = nvidia[i]
            if year == 2016 or year == 2019:
                self.prefix = "GTX"
            else:
                self.prefix = "RTX"
        elif self.manufacture.strip().lower() == "amd":
            for i in amd:
                if self.model in i:
                    year = amd[i]
            self.prefix = "RX"
        else:
            return self.__print_unknown()
        return self.__print_known(year)
