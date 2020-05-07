"""
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""

import copy


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None
        self.queue = []

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            self.queue.append(node)
        else:
            tree_node = self.queue[0]
            if tree_node.left is None:
                tree_node.left = node
                self.queue.append(node)
            else:
                tree_node.right = node
                self.queue.append(node)
                self.queue.pop(0)

    @staticmethod
    def level_recursive(root):
        if root is None:
            return None
        node = root
        queue = list()
        queue.append(node)
        while queue:
            node = queue.pop(0)
            if node.value is not None:
                yield node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def mirror(tree_root):
    if not tree_root:
        return None
    tree_root.right, tree_root.left = mirror(tree_root.left), mirror(tree_root.right)
    return tree_root


class Solution:
    def is_symmetrical(self, p_root_1, p_root_2):
        # write code here
        if p_root_2 and p_root_1:
            print(p_root_1.value, p_root_2.value)
        if not p_root_1 and not p_root_2:
            return True
        if p_root_1.value == p_root_2.value:
            return self.is_symmetrical(p_root_1.left, p_root_2.left) and self.is_symmetrical(p_root_1.right, p_root_2.right)
        return False


if __name__ == '__main__':
    tree = Tree()
    for i in [0, 1, 1, 2, 2, 2, 3]:
        tree.add(i)

    copy_tree = copy.deepcopy(tree)     # 类和list一样是可变对象
    s = Solution()
    print(s.is_symmetrical(copy_tree.root, mirror(tree.root)))