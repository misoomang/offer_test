"""
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = Node()

    def search_num(self, node, parent, value):
        if node is None:
            return False, node, parent
        if node.value == value:
            return True, node, parent
        if node.value > value:
            return self.search_num(node.left, node, value)
        else:
            return self.search_num(node.right, node, value)

    def insert_num(self, value):
        new_node = Node(value)
        if self.root.value is None:
            self.root = new_node
        else:
            flag, node, parent = self.search_num(self.root, self.root, value)
            if flag:
                return 'Ops! Has the same value node'
            else:
                if value < parent.value:
                    parent.left = new_node
                else:
                    parent.right = new_node

    def level(self, root):
        node_queue = [root]
        while node_queue:
            current_node = node_queue.pop(0)
            yield current_node.value
            if current_node.left is not None:
                node_queue.append(current_node.left)
            if current_node.right is not None:
                node_queue.append(current_node.right)


class Solution:
    # 返回对应节点TreeNode
    def k_th_node(self, p_root, k):
        # write code here
        node = p_root
        node_queue = list()
        i = 0
        while node_queue or node:
            while node:
                node_queue.append(node)
                node = node.left
            node = node_queue.pop()
            i += 1
            if i == k:
                return node.value
            node = node.right


if __name__ == '__main__':
    tree = Tree()
    for i in (5, 3, 7, 2, 4, 6, 8):
        tree.insert_num(i)

    level_num_list = list()
    for item in tree.level(tree.root):
        level_num_list.append(item)
    print(level_num_list)

    s = Solution()
    print(s.k_th_node(tree.root, 3))

