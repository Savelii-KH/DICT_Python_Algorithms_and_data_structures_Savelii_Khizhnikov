class GPU:
    manufacture: str
    model: int
    memory: int
    chip: str
    frequency: float
    videoresolution: str

    def __init__(self, manufacture: str, model: int, memory: int, chip: str, frequency: float, videoresolution: str):
        self.manufacture = manufacture
        self.model = model
        self.memorysize = memory
        self.graphicalchip = chip
        self.frequency = frequency
        self.videoresolution = videoresolution

        self.check()

    def check(self):
        nvidia = {(1030, 1050, 1060, 1070, 1080): 2016,
                  (2060, 2070, 2080): 2018,
                  (1650, 1660): 2019,
                  (3050, 3060, 3070, 3080, 3090): 2021}
        radeon = {(460, 470, 480): 2016,
                  (550, 560, 570, 580, 590): 2017,
                  (5500, 5600, 5700): 2019,
                  (6600, 6700, 6800, 6900): 2020}
        year: int = 0
        if self.manufacture.strip().lower() == "nvidia":
            for i in nvidia.keys():
                if self.model in i:
                    year = nvidia[i]
            if year == 2016 or year == 2019:
                model: str = f"GTX {self.model}"
            else:
                model: str = f"RTX {self.model}"
            self.info(year, model)
            return year, model
        elif self.manufacture.strip().lower() == "radeon":
            for i in radeon.keys():
                if self.model in i:
                    year = radeon[i]
            model: str = f"RX {self.model}"
            self.info(year, model)
            return year, model
        else:
            print(f"""{"-" * 70}
Подобная информация о видеокарте {self.model} от производителя {self.manufacture},
с графическим чипом {self.graphicalchip}
с такими характеристиками: 
объёмом памяти в {self.memorysize}GB, c частотой памяти {self.frequency} MHz 
и максимально допустимым разрешением экрана в {self.videoresolution} пикселей
Отсутствует.
{"-" * 70}""")

    def info(self, year, model):
        print(f"""{"-"*70}
Видеокарта {model} от производителя {self.manufacture},
с графическим чипом {self.graphicalchip}
выпущена в {year} году с такими характеристиками: 
объёмом памяти в {self.memorysize}GB, c частотой памяти {self.frequency} MHz 
и максимально допустимым разрешением экрана в {self.videoresolution} пикселей.
{"-"*70}""")


if __name__ == "__main__":
    gpu1 = GPU("Nvidia", 1080, 8, "GP104", 1733.0, "7680×4320")
    gpu2 = GPU("Troyan", 1480, 8, "XLS12", 1233.0, "3840×216")
    gpu3 = GPU("Radeon", 550, 4, "Polaris 12", 1182.0, "3840×2160")
    gpu4 = GPU("Radeon", 6600, 8, "Navi 23 XL", 2359.0, "7680×4320")
    # gpu5 = GPU(123, 3123, 13421, 1414, 134, 324)
