"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class Node:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left


def reconstruct_binary_tree(pre, tin):
    """
    :param pre: 前序遍历数组(根左右)
    :param tin: 中序遍历数组(左根右)
    :return:
    """
    if not pre:
        return None
    root_value = pre[0]     # 获取根节点
    root_index = tin.index(root_value)      # 获取根节点在中序遍历的位置
    root = Node(root_value)
    root.left = reconstruct_binary_tree(pre[1: root_index+1], tin[:root_index])
    root.right = reconstruct_binary_tree(pre[root_index+1:], tin[root_index+1:])
    return root


def qianxu(tree_root):
    if tree_root is None:
        return
    node = tree_root
    node_queue = []
    while node_queue or node:
        while node:
            yield node.value
            node_queue.append(node)
            node = node.left
        node = node_queue.pop()
        node = node.right


def zhongxu(tree_root):
    if tree_root is None:
        return
    node = tree_root
    node_queue = []
    while node_queue or node:
        while node:
            node_queue.append(node)
            node = node.left
        node = node_queue.pop()
        yield node.value
        node = node.right


def houxu(tree_root):
    if tree_root is None:
        return
    node_queue_1 = []
    node_queue_2 = []
    node = tree_root
    node_queue_1.append(node)
    while node_queue_1:
        node = node_queue_1.pop()
        if node.left:
            node_queue_1.append(node.left)
        if node.right:
            node_queue_1.append(node.right)
        node_queue_2.append(node)
    while node_queue_2:
        node = node_queue_2.pop()
        yield node.value


if __name__ == '__main__':
    root_tree = reconstruct_binary_tree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    qianxu_list = []
    for i in qianxu(root_tree):
        qianxu_list.append(i)
    print('前序遍历', qianxu_list)

    zhongxu_list = []
    for i in zhongxu(root_tree):
        zhongxu_list.append(i)
    print('中序遍历', zhongxu_list)

    houxu_list = []
    for i in houxu(root_tree):
        houxu_list.append(i)
    print('后序遍历', houxu_list)
