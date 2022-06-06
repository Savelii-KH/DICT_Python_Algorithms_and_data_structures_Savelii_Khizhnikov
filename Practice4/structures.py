from AbstractLimitStructure import AbstractStack
from AbstractLimitStructure import AbstractQueue
from Practice2.generator import Generator
from Practice2.gpu import GPU
from node import Node


class Stack(AbstractStack):
    __node = Node(None)
    __head = __node
    __cur_top = __head

    def push(self, value: GPU) -> bool:
        head = self.__head
        top = self.__head.n
        new_el = Node(value)
        head.n = new_el
        new_el.n = top
        self.__cur_top = head.n

        return True

    def pop(self) -> [GPU, None]:
        if self.__head.n is not None:
            head = self.__head
            top = head.n
            new_top = top.n
            head.n = new_top
            self.__cur_top = new_top
            return top.data
        else:
            return None

    def top(self) -> [GPU, None]:
        if self.__cur_top is not None:
            return self.__cur_top.data
        else:
            return None


class Queue(AbstractQueue):
    __body = []
    __size = 0

    def enqueue(self, value: GPU) -> bool:
        self.__body.append(value)
        self.__size += 1
        return True

    def dequeue(self) -> [GPU, None]:
        if self.__size != 0:
            value = self.__body[0]
            self.__body.remove(value)
            self.__size -= 1
            return value
        else:
            return None

    def top(self) -> [GPU, None]:
        if self.__size != 0:
            return self.__body[0]
        else:
            return None


s = Stack()
q = Queue()
g = Generator()

print(f"{'*' * 25}STACK{'*' * 25}")
s.push(g.generator())
s.push(g.generator())
s.push(g.generator())
s.push(g.generator())
s.push(g.generator())

print(f"top : {s.top()}")

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

print(f"top : {s.top()}")

print(f"{'*' * 25}QUEUE{'*' * 25}")
q.enqueue(g.generator())
q.enqueue(g.generator())
q.enqueue(g.generator())
q.enqueue(g.generator())
q.enqueue(g.generator())

print(f"top : {q.top()}")

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

print(f"top : {q.top()}")
