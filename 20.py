"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。
思路：时间复杂度为O(1)说明不能对本身堆栈进行遍历(不能用for循环或while循环获取最小元素)
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, node):
        self.stack.append(node)
        if not self.mini:
            self.mini.append(node)
        else:
            if self.mini[0] > node:
                self.mini.insert(0, node)
            else:
                self.mini.append(node)

    def pop(self):
        num = self.stack.pop()
        index = self.mini.index(num)
        self.mini.pop(index)

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return []

    def min(self):
        return self.mini[0]


if __name__ == '__main__':
    solution = Solution()
    for i in range(5):
        solution.push(i)
    solution.pop()
    print(solution.top())
    print(solution.min())
