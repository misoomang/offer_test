"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
还是斐波那契
"""


def fibo(number: int):
    if number == 0:
        return 0
    if number == 1 or number == 2:
        return 1
    a, b = 0, 1
    i = 2
    while i <= number:
        a, b = b, a + b
        i += 1
    return a


if __name__ == '__main__':
    print(fibo(6))
