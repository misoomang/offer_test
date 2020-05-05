"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
思路：中序遍历（左根右）
"""


class Solution:
    def GetNext(self, p_node):
        # write code here
        if not p_node:
            return None
        if p_node.right:            # 存在右子树
            node = p_node.right
            while node:
                node = node.left
            return node
        elif p_node.parent and p_node.right == p_node:      # 没有右子树，且该节点为其父节点的右子树
            p_node = p_node.parent.parent
        else:
            p_node = p_node.parent      # 下一个节点即为其父节点
        return p_node




