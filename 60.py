"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None
        self.queue = list()

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
    def level_recursive(root):
        node_queue = [root]
        while node_queue:
            temp = list()
            for item in range(len(node_queue)):
                current_node = node_queue.pop(0)
                if current_node is not None:
                    temp.append(current_node.value)
                if current_node.left is not None:
                    node_queue.append(current_node.left)
                if current_node.right is not None:
                    node_queue.append(current_node.right)
            print(temp)

if __name__ == '__main__':
    tree = Tree()
    for i in range(6):
        tree.add(i)
    tree.level_recursive(tree.root)
