"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
"""


def is_pop_order(push_stack, pop_stack):
    stack = list()
    i = 0
    for item in push_stack:
        stack.append(item)
        while stack and stack[-1] == pop_stack[i]:
            i += 1
            stack.pop(-1)
    if not stack:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_pop_order([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
    print(is_pop_order([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
