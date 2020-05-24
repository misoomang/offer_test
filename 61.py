# -*- coding:utf-8 -*-
"""
请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，
序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

例如，我们可以把一个只有根节点为1的二叉树序列化为"1,"，然后通过自己的函数来解析回这个二叉树
"""



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.root = None
        self.queue = list()

    def Serialize(self, root):
        # write code here
        s = ''
        node_queue = list()
        node_queue.append(root)
        while node_queue:
            current_node = node_queue.pop(0)
            if current_node is not None:
                s += str(current_node.val) + '!'
            else:
                s += '#'
            if current_node.left is not None:
                node_queue.append(current_node.left)
            if current_node.right is not None:
                node_queue.append(current_node.right)
        return s

    def Deserialize(self, s):
        # write code here
        str_list = s.split('!')

        for val in str_list:
            node = TreeNode(val)
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
        return self.root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    s = Solution()
    print_s = s.Serialize(root)
    print(print_s)

    de_root = s.Deserialize(print_s)
    print(de_root.val)
    print(de_root.left.val)
    print(de_root.right.val)
    print(de_root.left.left.val)
    print(de_root.left.right.val)

