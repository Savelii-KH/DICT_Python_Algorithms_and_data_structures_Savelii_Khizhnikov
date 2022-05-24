from Practice2.gpu import GPU


class Node:

    def __init__(self, data: GPU):
        self.data = data    # type: GPU
        self.next = None    # type: [Node, None]

    def has_value(self, value: GPU):
        """method to compare the value with the node data"""
        if self.data is value:
            return True
        else:
            return False

    def __repr__(self):
        return self.data
