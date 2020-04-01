"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node


class ArrayList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def is_empty(self):
        if self._length == 0:
            return True
        else:
            return False

    def insert_node(self, value):
        node = Node(value)
        node.set_next(self._head)
        self._head = node
        self._length += 1

    def append(self, value):
        node = Node(value)
        if self.is_empty():
            self._head = node
            self._length += 1
        else:
            current_node = self._head
            while current_node is not None:
                current_node = current_node.get_next()
            current_node.set_next(node)
            self._length += 1

    def read(self):
        current_node = self._head
        if not current_node:
            return
        while current_node is not None:
            yield current_node.get_value()
            current_node = current_node.get_next()


if __name__ == '__main__':
    array_list = ArrayList()
    for i in range(7):
        array_list.insert_node(i)

    for n in array_list.read():
        print(n)
