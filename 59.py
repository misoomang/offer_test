"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
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


class Solution:
    @staticmethod
    def printf(p_root):
        result = list()
        node_queue = list()
        node_queue.append(p_root)
        i = 1           # 第一层
        while node_queue:
            temp_result = list()
            for n in range(len(node_queue)):
                node = node_queue.pop(0)
                if node is not None:
                    temp_result.append(node.value)
                if node.left is not None:
                    node_queue.append(node.left)
                if node.right is not None:
                    node_queue.append(node.right)

            if i % 2 == 0:      # 偶数层
                temp_result.reverse()
            result.extend(temp_result)
            i += 1
        return result


if __name__ == '__main__':
    tree = Tree()
    for j in range(15):
        tree.add(j)

    solution = Solution()
    print(solution.printf(tree.root))





