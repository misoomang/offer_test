"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树

平衡二叉树特性：在符合二叉树的前提下，左右子树高度相差不大于1
"""


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def get_depth(self, root):
        if root is None:
            return 0
        left_depth = self.get_depth(root.left)
        if left_depth == -1:
            return -1
        right_depth = self.get_depth(root.right)
        if right_depth == -1:
            return -1
        if abs(left_depth - right_depth) > 1:           # 左右子树高度是否大于1
            return -1
        return 1 + max(left_depth, right_depth)

    def is_balanced_solution(self, root):
        return self.get_depth(root) != -1


if __name__ == '__main__':
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node0.left = node1
    node0.right = node2
    node1.left = node3
    node3.left = node4
    s = Solution()
    print(s.is_balanced_solution(node0))

