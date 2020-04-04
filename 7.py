"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""


def jump(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    print(jump(3))

