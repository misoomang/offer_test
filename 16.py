"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
思路：A子结构与B进行对比，子结构为A左子树，A左子树的左子树，A左子树的左子树的左子树。。。递归
                          子结构为A右子树，A左子树的右子树，A左子树的右子树的右子树。。。递归
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


def compare(sub_tree_a, sub_tree_b):
    if sub_tree_a is None and sub_tree_b:
        return False
    elif sub_tree_b is None:
        return True
    elif sub_tree_a.value != sub_tree_b.value:
        return False
    else:
        return compare(sub_tree_a.left, sub_tree_b.left) and compare(sub_tree_a.right, sub_tree_b.right)


flag = False


def has_sub_tree(tree_a, tree_b):
    if tree_a and tree_b:
        if tree_a.value == tree_b.value:
            global flag
            flag = compare(tree_a, tree_b)
        if flag:
            return True
        else:
            return has_sub_tree(tree_a.left, tree_b) or has_sub_tree(tree_a.right, tree_b)
    else:
        return flag


if __name__ == '__main__':
    a_tree = Tree()
    for i in range(0, 6):
        a_tree.add(i)

    b_tree = Tree()
    for i in [2, 5]:
        b_tree.add(i)

    c_tree = Tree()
    for i in [1, 3, 4]:
        c_tree.add(i)

    print(has_sub_tree(a_tree.root, b_tree.root))
    print(has_sub_tree(a_tree.root, c_tree.root))
