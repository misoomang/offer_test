"""
输入一个链表，输出该链表中倒数第k个结点。
思路一：先获得链表的整体长度n，倒数第k个节点，则正数为第n-k+1个节点(k<=n)
思路二：快慢指针，快指针找到第k-1个节点，慢指针指向第1个节点，共同向后指向下一个节点
        当快指针指向最后一个节点时，慢指针即指向倒数第k个节点
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


def find_kth_to_tail_1(array_list, k):
    if array_list.length < k:
        return 'k大于链表长度'
    tmp_length = array_list.length - k
    tmp_node = array_list.head
    while tmp_length:
        tmp_node = tmp_node.next_node
        if tmp_node:
            tmp_length -= 1
    return tmp_node.value


def find_kth_to_tail_2(array_list, k):
    fast_node = array_list.head
    slow_node = array_list.head
    for _ in range(k):
        if fast_node:
            fast_node = fast_node.next_node   # 获取第k-1个r节点
    while fast_node:
        fast_node = fast_node.next_node
        slow_node = slow_node.next_node
    return slow_node.value


if __name__ == '__main__':
    array = Array()
    for i in range(1, 7):
        array.add(i)                # array 为 6 5 4 3 2 1
    print(find_kth_to_tail_1(array, 4))
    print(find_kth_to_tail_2(array, 4))
