"""
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Solution:
    def __init__(self):
        self.queue_node = list()

    @staticmethod
    def delete_duplication(p_head):
        # write code here
        pre = p_head
        current = p_head.next_node
        while current and current.next_node:
            if current.value == current.next_node.value:        # 出现重复数字
                while current.value == current.next_node.value:     # 处理连续出现重复数字，如 3 3 3 3 3 3 3...获取到最后出现3的位置
                    current.next_node = current.next_node.next_node
                pre.next_node = current.next_node
                current = current.next_node
            else:
                pre = current
                current = current.next_node
        return p_head


if __name__ == '__main__':
    p_head = Node(1)
    p_head.next_node = Node(2)
    p_head.next_node.next_node = Node(3)
    p_head.next_node.next_node.next_node = Node(3)
    p_head.next_node.next_node.next_node.next_node = Node(4)
    p_head.next_node.next_node.next_node.next_node.next_node = Node(4)
    p_head.next_node.next_node.next_node.next_node.next_node.next_node = Node(5)
    s = Solution()
    deleted_head = s.delete_duplication(p_head)
    node = deleted_head
    while node:
        print(node.value)
        node = node.next_node
