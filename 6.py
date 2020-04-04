"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
0 1 1 2 3 5 8
"""


def fibo(number: int):
    a, b = 0, 1
    i = 2
    while i <= number:
        a, b = b, a+b
        i += 1
    return a

if __name__ == '__main__':
    print(fibo(39))
