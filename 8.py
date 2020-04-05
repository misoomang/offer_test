"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
思路：
青蛙第一次可以跳1级，还剩F(n-1)
青蛙第一次可以跳2级，还剩F(n-2)
...
青蛙第一次可以跳n-1级，还剩1级
青蛙第一次可以跳n级，还剩0级
共    F(n) = F(n-1) + F(n-2) + ... + 2 + 1
同理：F(n-1) = F(n-2) + ... + 2 + 1
故F(n) = 2F(n-1)
"""


def jump(number: int):
    if number == 1:
        return 1
    if number == 2:
        return 2
    return 2 * jump(number - 1)


"""
F(n) = 2F(n-1) = 2 * 2F(n-2) = 2^2 * F(n-2) = ... = 2^(n-1) * F(1)
"""


def jump_1(number: int):
    return 2 ** (number - 1)


if __name__ == '__main__':
    print(jump(5))
    print(jump_1(5))
