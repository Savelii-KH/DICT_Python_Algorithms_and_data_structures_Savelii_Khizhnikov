class GPU:
    manufacture: str
    model: str
    memorysize: str
    graphicalchip: str
    frequency: str
    videoresolution: str

    def __init__(self, manufacture: str, model: str, memorysize: str, graphicalchip: str, frequency: str, videoresolution: str):
        self.manufacture = manufacture
        self.model = model
        self.memorysize = memorysize
        self.graphicalchip = graphicalchip
        self.frequency = frequency
        self.videoresolution = videoresolution

        self.check()

    def check(self):
        nvidia = {("1030", "1050", "1060", "1070", "1080"): "2016",
                  ("2060", "2070", "2080"): "2018",
                  ("1650", "1660"): "2019",
                  ("3050", "3060", "3070", "3080", "3090"): "2021"}
        radeon = {("460", "470", "480"): "2016",
                  ("550", "560", "570", "580", "590"): "2017",
                  ("5500", "5600", "5700"): "2019",
                  ("6600", "6700", "6800", "6900"): "2020"}
        year = None
        model = "".join(list(self.model)).split()
        if self.manufacture == "Nvidia":
            for i in nvidia.keys():
                if model[1] in i:
                    year = nvidia.get(i)
                    self.info(year)
            return year
        elif self.manufacture == "Radeon":
            for i in radeon.keys():
                if model[1] in i:
                    year = radeon.get(i)
                    self.info(year)
            return year
        else:
            print(f"""{"-"*70}
Подобная информация о видеокарте {self.model} от производителя {self.manufacture},
с графическим чипом {self.graphicalchip}
выпущена в {year} году с такими характеристиками: 
объёмом памяти в {self.memorysize},
и максимально допустимым разрешением экрана в {self.videoresolution} пикселей
Отсутствует.
{"-"*70}""")

    def info(self, year):
        print(f"""{"-"*70}
Видеокарта {self.model} от производителя {self.manufacture},
с графическим чипом {self.graphicalchip}
выпущена в {year} году с такими характеристиками: 
объёмом памяти в {self.memorysize},
и максимально допустимым разрешением экрана в {self.videoresolution} пикселей.
{"-"*70}""")


if __name__ == "__main__":
    gpu1 = GPU("Nvidia", "GTX 1080", "8GB", "GP104", "1733 MHz", "7680×4320")
    gpu2 = GPU("Troyan", "HTE 1480", "8GB", "XLS12", "1233 MHz", "3840×216")
    gpu3 = GPU("Radeon", "Rx 550", "4GB", "Polaris 12", "1182 MHz", "3840×2160")
    gpu4 = GPU("Radeon", "Rx 6600", "8GB", "Navi 23 XL", "2359 MHz", "7680×4320")
    gpu5 = GPU(123, 3123, 13421, 1414, 134, 324)
