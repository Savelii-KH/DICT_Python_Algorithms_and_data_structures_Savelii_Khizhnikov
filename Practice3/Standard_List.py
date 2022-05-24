from AbstractStructure import AbstractStructure
from Practice2.generator import Generator
from Practice2.gpu import GPU


class StandardList2(AbstractStructure):
    __list: list = []
    size: int = 0

    def add(self, value: GPU, index: [int, None] = None) -> bool:
        if index is not None and self.size <= index < -self.size:
            return False
        if index is None:
            self.__list.append(value)
        else:
            self.__list.insert(index, value)
        self.size += 1
        return True

    def insert(self, value: GPU, index: int) -> bool:
        if (index is not None and self.size <= index < -self.size) or index is None:
            return False
        self.__list[index] = value
        return True

    def find(self, value: GPU) -> [int, None]:
        if value in self.__list:
            return self.__list.index(value)
        return None

    def get(self, index: int) -> [GPU, None]:
        if -self.size < index <= self.size:
            return self.__list[index]
        return None

    def remove(self, value: GPU) -> bool:
        if value in self.__list:
            self.__list.remove(value)
            self.size -= 1
            return True
        return False

    def get_all(self) -> list:
        return self.__list

    def __len__(self) -> int:
        return self.size


if __name__ == "__main__":
    g = Generator()
    gpu1 = g.generator()
    gpu2 = g.generator()
    gpu3 = g.generator()
    gpu4 = g.generator()
    gpu5 = g.generator()
    gpu6 = g.generator()
    print([gpu1, gpu2, gpu3, gpu4, gpu5, gpu6])
    print("-" * 300)
    s_list = StandardList2()
    print(f"add1: {s_list.add(gpu1)}")
    print(f"add2: {s_list.add(gpu2)}")
    print(f"add3: {s_list.add(gpu3)}")
    print(f"add4: {s_list.add(gpu4)}")
    print(f"add5: {s_list.add(gpu5)}")
    print("-" * 300)
    print(f"insert: {s_list.insert(gpu6, 1)}")
    print(f"get_all1: {s_list.get_all()}")
    print(f"len1: {len(s_list)}")
    print("-" * 300)
    print(f"find gpu1: {s_list.find(gpu1)}")
    print(f"find gpu2: {s_list.find(gpu2)}")
    print("-" * 300)
    print(f"get1: {s_list.get(1)}")
    print("-" * 300)
    print(f"remove gpu3: {s_list.remove(gpu3)}")
    print(f"remove gpu3: {s_list.remove(gpu3)}")
    print(f"get_all2: {s_list.get_all()}")
    print(f"len2: {len(s_list)}")
