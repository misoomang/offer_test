"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0的前提下
"""


def power(base, exponent):
    if exponent == 0:       # 指数为0时结果均为1
        return 1
    abs_exponent = abs(exponent)
    tmp = base
    while abs_exponent - 1:
        abs_exponent -= 1
        base *= tmp
    if exponent > 0:
        return base
    if exponent < 0:
        return 1 / base


if __name__ == '__main__':
    print(power(2, 5))
    print(power(0.2, -1))
