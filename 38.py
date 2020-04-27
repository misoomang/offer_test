"""
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""


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
            current_node = self.queue[0]
            if current_node.left is None:
                current_node.left = node
                self.queue.append(current_node.left)
            else:
                current_node.right = node
                self.queue.append(current_node.right)
                self.queue.pop()

    @staticmethod
    def tree_depth(root):
        node = root
        node_list = list()
        node_list.append(node)
        depth = 1
        while node_list:
            current_node = node_list.pop(0)
            if current_node.left is not None:
                node_list.append(current_node.left)
            if current_node.right is not None:
                node_list.append(current_node.left)
            depth += 1
        return depth


if __name__ == '__main__':
    tree = Tree()
    for i in range(8):
        tree.add(i)
    print(tree.tree_depth(tree.root))
