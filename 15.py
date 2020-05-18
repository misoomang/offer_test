"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next(self, node):
        self.next_node = node


class Array:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, value):
        node = Node(value)
        node.set_next(self.head)
        self.head = node
        self.length += 1

    def print_num(self):
        node = self.head
        while node:
            yield node.value
            node = node.next_node


def merge_link_list(first_link_list, second_link_list):
    res = Node(0)
    head = res
    first_link_node = first_link_list.head
    second_link_node = second_link_list.head
    while first_link_node and second_link_node:
        # print(first_link_node.value, second_link_node.value)
        if first_link_node.value < second_link_node.value:
            if head is None:
                head = first_link_node
                first_link_node = first_link_node.next_node
            else:
                head.next_node = first_link_node
                head = head.next_node
                first_link_node = first_link_node.next_node
        else:
            if head is None:
                head = second_link_node
                second_link_node = second_link_node.next_node
            else:
                head.next_node = second_link_node
                head = head.next_node
                second_link_node = second_link_node.next_node

    if first_link_node:
        head.next_node = first_link_node
    if second_link_node:
        head.next_node = second_link_node
    return res.next_node


if __name__ == '__main__':
    link_list_1 = Array()
    for i in range(11, 4, -2):
        link_list_1.add(i)

    array_list = []
    for value in link_list_1.print_num():
        array_list.append(value)
    print(array_list)

    link_list_2 = Array()
    for i in range(17, 1, -2):
        link_list_2.add(i)

    array_list = []
    for value in link_list_2.print_num():
        array_list.append(value)
    print(array_list)
    merged_link = merge_link_list(link_list_1, link_list_2)

    merge_array_list = []
    node = merged_link
    while node:
        merge_array_list.append(node.value)
        node = node.next_node
    print(merge_array_list)
