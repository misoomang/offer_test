"""
输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
思路：获取两个链表的长度n，较长长度从第n+1个节点开始，较短长度链表从第1个节点开始，同时向后遍历，直到两者到达相同节点几位公共节点
"""


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


def find_first_common_node(p_head1, p_head2):
    # write code here
    head1_length = 0
    head2_length = 0
    node1 = p_head1
    node2 = p_head2
    while node1:
        head1_length += 1
        node1 = node1.next_node

    while node2:
        head2_length += 1
        node2 = node2.next_node

    print(head1_length, head2_length)
    if head1_length >= head2_length:
        current_node = p_head1
        for i in range(head1_length - head2_length):
            current_node = current_node.next_node
        smaller_head = p_head2
    else:
        current_node = p_head2
        for i in range(head2_length - head1_length):
            current_node = current_node.next_node
        smaller_head = p_head1

    while smaller_head and current_node:
        if smaller_head == current_node:
            return smaller_head
        else:
            smaller_head = smaller_head.next_node
            current_node = current_node.next_node


if __name__ == '__main__':
    p_head1 = Node(1)
    p_head1.next_node = Node(2)
    p_head1.next_node.next_node = Node(3)
    p_head1.next_node.next_node.next_node = Node(4)
    p_head1.next_node.next_node.next_node.next_node = Node(5)
    p_head1.next_node.next_node.next_node.next_node.next_node = Node(6)
    p_head1.next_node.next_node.next_node.next_node.next_node.next_node = Node(7)
    p_head1.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(8)

    p_head2 = Node('a')
    p_head2.next_node = Node('b')
    p_head2.next_node.next_node = Node('c')
    p_head2.next_node.next_node.next_node = Node('d')
    p_head2.next_node.next_node.next_node.next_node = Node('e')
    p_head2.next_node.next_node.next_node.next_node.next_node = Node('f')
    p_head2.next_node.next_node.next_node.next_node.next_node.next_node = p_head1.next_node.next_node.next_node.next_node

    common_node = find_first_common_node(p_head1, p_head2)
    print(common_node.value)



