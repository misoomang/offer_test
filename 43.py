"""
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
思路：YX = (X的转置 Y的转置)的转置
"""


def left_rotate_string(s, n):
    return s[n:] + s[:n]


def reverse(string, start, end):
    """

    :param string: 需要转置的字符串
    :param start: 转置的开始位置
    :param end: 转置的结束位置
    :return:
    """
    if start == 0:
        return string[start: end][::-1] + string[end:]
    else:
        return string[0: start] + string[start: end][::-1]


def left_rotate_string_1(s, n):
    if not s or n == 0:
        return s
    s = list(s)
    s = reverse(s, 0, n)            # 前半部分转置
    s = reverse(s, n, len(s))       # 后半部分转置
    s = reverse(s, 0, len(s))       # 整体转置
    return ''.join(s)


if __name__ == '__main__':
    print(left_rotate_string('abcXYZdef', 3))
    print(left_rotate_string_1('abcXYZdef', 3))
