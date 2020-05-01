"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
经查看资料：
13 + 11
13二进制：1 1 0 1   记为a
11二进制：1 0 1 1   记为b
(a&b)<<1    1 0 0 1 0 记为d
a^b           0 1 1 0 记为e

(d&e)<<1    0 0 1 0 0   记为f
d^e         1 0 1 0 0   记为g

(f&g)<<1    0 1 0 0 0   记为h
f^g ->      1 0 0 0 0   记为i
(h&i)<<1   0 0 0 0 0   记为h  0 ---- --------退出循环
h^i        1 1 0 0 0  记为i   24
"""


def add(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    while num1 != 0:
        a = (num1 & num2) << 1
        b = num1 ^ num2
        num1 = a
        num2 = b
    return num2


if __name__ == '__main__':
    print(add(13, 11))
