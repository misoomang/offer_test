"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""


class Node:
    def __init__(self, elem=None, left=None, right=None):
        self.elem = elem
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
                self.queue.pop(0)

    @staticmethod
    def print_from_top_to_bottom(root):
        if root is None:
            return None
        else:
            queue = []
            node = root
            queue.append(node)
            while queue:
                node = queue.pop(0)
                if node is not None:
                    yield node.elem
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


if __name__ == '__main__':
    tree = Tree()
    for i in [1, 2, 3, 4, 5, 6]:
        tree.add(i)

    level_recursive = list()
    for j in tree.print_from_top_to_bottom(tree.root):
        level_recursive.append(j)
    print(level_recursive)
