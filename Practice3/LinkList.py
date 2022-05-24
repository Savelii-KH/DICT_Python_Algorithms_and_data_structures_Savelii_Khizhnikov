from AbstractStructure import AbstractStructure
from Practice2.generator import Generator
from Practice2.gpu import GPU
from Node import Node


class LinkList(AbstractStructure):
    __head: [None, Node] = None
    __tail: [None, Node] = None
    size: int = 0

    def add(self, value: GPU, index: [None, int] = None) -> bool:
        if index is not None and (index < 0 or index > self.size):
            return False
        if self.__head is None:
            node = Node(value)
            self.__head = node
            self.__tail = node
            self.size += 1
        elif index is None:
            current = self.__tail
            node = Node(value)
            current.next = node
            self.__tail = node

            # current = self.__head
            # while current.next:
            #     current = current.next
            # current.next = Node(value)
            self.size += 1
        else:
            i = 0
            current = self.__head
            while current.next and i < index - 1:
                current = current.next
                i += 1
            self.size += 1
            node = Node(value)
            node.next = current.next
            current.next = node
        return True

    def insert(self, value: GPU, index: int) -> bool:
        if index is not None and (index < 0 or index >= self.size):
            return False
        else:
            i = 0
            current = self.__head
            while current.next and i < index - 1:
                current = current.next
                i += 1
            node = Node(value)
            node.next = current.next
            current.next = node
        return True

    def find(self, value: GPU) -> [int, None]:
        i = 0
        current = self.__head
        try:
            while current.data != value:
                current = current.next
                i += 1
            return i
        except AttributeError:
            return None

    def get(self, index: int) -> object:
        if self.size <= index or index < 0:
            return None
        else:
            i = 0
            current = self.__head
            while current.next and i < index:
                current = current.next
                i += 1
            return current.data

    def remove(self, value: GPU) -> bool:
        current = self.__head
        if current is None:
            return False
        while current:
            try:
                if current.next.data == value:
                    current.next = current.next.next
                    break
            except AttributeError:
                pass
            if current.data == value:
                self.__head = current.next
                break
            current = current.next
        self.size -= 1
        return True

    def get_all(self) -> list:
        output = []
        current = self.__head
        while current is not None:
            output.append(current.data)
            current = current.next
        return output


if __name__ == "__main__":
    g = Generator()
    gpu1 = g.generator()
    gpu2 = g.generator()
    gpu3 = g.generator()
    gpu4 = g.generator()
    gpu5 = g.generator()
    gpu6 = g.generator()
    s_list = LinkList()
    s_list.add(gpu1)
    s_list.add(gpu2)
    s_list.add(gpu3)
    s_list.add(gpu4)
    print(f"add: {s_list.add(gpu5, 0)}")
    print(f"all GPUs: {[gpu1, gpu2, gpu3, gpu4, gpu5, gpu6]}")
    print(f"get_all:  {s_list.get_all()}")
    print(f"size: {s_list.size}")
    print(f"remove: {s_list.remove(gpu5)}")
    print(f"get_all:  {s_list.get_all()}")
    print(f"size: {s_list.size}")
    print(f"get gpu1: {s_list.get(0)}")
    print(f"get gpu4: {s_list.get(3)}")
    print(f"get gpu5: {s_list.get(4)}")
    print(f"insert: {s_list.insert(gpu6, 1)}")
    print(f"get_all:  {s_list.get_all()}")
    print(f"size: {s_list.size}")
    print(f"find: {s_list.find(gpu5)}")
