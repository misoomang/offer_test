"""输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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
                self.queue.append(tree_node.left)
            else:
                tree_node.right = node
                self.queue.append(tree_node.right)
                self.queue.pop(0)

    # 二叉搜索树中序遍历为从小到大（左根右）
    @staticmethod
    def convert(root):
        if root is None:
            return
        node_queue = []
        node = root
        is_first = True
        pre = None
        while node or node_queue:
            while node:
                node_queue.append(node)
                node = node.left
            node = node_queue.pop()
            if is_first:        # 双向链表头部
                root = node
                pre = root
                is_first = False
            else:               # 加入后续链表节点，改变前后指针指向
                pre.right = node
                node.left = pre
                pre = node
            node = node.right
        return root


if __name__ == '__main__':
    tree = Tree()
    for i in [5, 3, 7, 2, 4, 6, 8]:         # 构建二叉排序树
        tree.add(i)
    convert_root = tree.convert(tree.root)
    print(convert_root.value)
    print(convert_root.right.value)
    print(convert_root.right.right.value)
    print(convert_root.right.left.value)
