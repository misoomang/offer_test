"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
思路一：用数组记录所遍历的链表，若出现重复节点，则为环入口
思路二：用快慢指针，慢指针每次遍历一个节点，快指针每次遍历两个节点，当快指针==慢指针时，让慢指针指向头指针，快指针从相遇指针位置同时向后遍历
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Solution:
    def __init__(self):
        self.node_queue = []

    def entry_node_of_loop(self, p_head):
        # write code here
        node = p_head
        while node is not None:
            if node not in self.node_queue:
                self.node_queue.append(node)
            else:
                return node
            node = node.next_node
        return None

    @staticmethod
    def entry_node_of_loop_1(p_head):
        slow = p_head
        fast = p_head
        while True:
            if fast and fast.next_node:
                slow = slow.next_node
                fast = fast.next_node.next_node
                if fast == slow:
                    slow = p_head
                    while slow != fast:
                        slow = slow.next_node
                        fast = fast.next_node
                        if slow == fast:
                            return fast
        return None


if __name__ == '__main__':
    p_head = Node(0)
    p_head.next_node = Node(1)
    p_head.next_node.next_node = Node(2)
    p_head.next_node.next_node.next_node = Node(3)
    p_head.next_node.next_node.next_node.next_node = Node(4)
    p_head.next_node.next_node.next_node.next_node.next_node = Node(5)
    p_head.next_node.next_node.next_node.next_node.next_node.next_node = Node(6)
    p_head.next_node.next_node.next_node.next_node.next_node.next_node.next_node = p_head.next_node
    s = Solution()
    loop_node = s.entry_node_of_loop(p_head)
    if loop_node:
        print(loop_node.value)

    loop_node_q = s.entry_node_of_loop_1(p_head)
    if loop_node_q:
        print(loop_node_q.value)
