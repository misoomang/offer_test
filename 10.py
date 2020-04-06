"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
思路一：转二进制，再转字符串，为1计数
思路二：n为3时，3 & 2 = 2， 2 & 1 = 0，次数为2，故二进制2个1
        n为4时，4 & 3 = 0，次数为1，故有二进制有1个1
        n为5时，5 & 4 = 4， 4 & 3 = 0，故二进制有2个1
"""

from ctypes import *
"""
c_int是为了解决负数问题
"""


def number_of_1(number: int):
    str_num = str(bin(number))
    if '1' in str_num:
        return str_num.count('1')
    return 0


def number_of_2(n):
    cnt = 0
    while c_int(n).value:
        n = n & (n-1)
        cnt += 1
    return cnt


if __name__ == '__main__':
    print(number_of_1(5))
    print(number_of_2(5))
