"""
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
思路：如果expect_number - node.value == 0 且没有左右子树，则返回；否则expect_number -= root.value
      如果expect_number - node.value == 0 且没有左右子树，则返回；否则expect_number -= root.value。。。递归
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

tmp_list = list()
path_list = list()


def find_path(node, expect_number):
    if node is None:
        return []
    tmp_list.append(node.elem)
    print(tmp_list)
    expect_number -= node.elem
    if expect_number == 0 and not node.left and not node.right:
        path_list.extend(tmp_list)
    find_path(node.left, expect_number)
    find_path(node.right, expect_number)
    tmp_list.pop()          # 到底部回退一个子节点
    return path_list


if __name__ == '__main__':
    tree = Tree()
    for i in range(0, 7):
        tree.add(i)
    find_path(tree.root, 5)
    print(path_list)




