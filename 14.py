"""
输入一个链表，反转链表后，输出新链表的表头。
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next(self, node):
        self.next_node = node

    def get_next(self):
        return self.next_node


class LinkList:
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def add(self, value):
        node = Node(value)
        node.next_node = self.head
        self.head = node
        self.length += 1


def reverse_link_list(link_list):
    head = link_list.head
    pre = None
    current = head
    while current is not None:
        next_node = current.next_node
        current.next_node = pre
        pre = current
        current = next_node
    return pre.value


if __name__ == '__main__':
    link_list = LinkList()
    for i in range(1, 7):
        link_list.add(i)
    print(reverse_link_list(link_list))
