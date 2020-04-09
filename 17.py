"""
操作给定的二叉树，将其变换为源二叉树的镜像。
"""

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    """
    创建二叉树
    """
    def __init__(self):
        self.root = Node()
        self.queue = []

    def add(self, value):
        node = Node(value)
        if self.root.value is None:
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


def mirror(node):
    if node is None:
        return None
    node.right, node.left = mirror(node.left), mirror(node.right)
    return node
    # if node.left and node.right:
    #     node.left, node.right = node.right, node.left
    #     mirror(node.left)
    #     mirror(node.right)
    # elif node.left:
    #     node.right = node.left
    #     mirror(node.left)
    #     node.left = None
    # elif node.right:
    #     node.left = node.right
    #     mirror(node.right)
    #     node.right = None


if __name__ == '__main__':
    tree = Tree()
    for i in range(0, 6):
        tree.add(i)

    before = list()
    after = list()
    for i in tree.level_recursive(tree.root):
        before.append(i)
    print(before)
    mirror(tree.root)
    for i in tree.level_recursive(tree.root):
        after.append(i)
    print(after)
