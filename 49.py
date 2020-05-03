"""
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。
数值为0或者字符串不是一个合法的数值则返回0。
输入描述: 输入一个字符串,包括数字字母符号,可以为空
输出描述: 如果是合法的数值表达则返回该数字，否则返回0
"""


def str_to_int(s):
    if not s:
        return
    is_positive = 1         # 正负
    result = 0
    flag = True             # 判断是否符合条件
    for i in range(len(s)):
        if i == 0 and s[0] == '+':
            is_positive = 1
        elif i == 0 and s[i] == '-':
            is_positive = -1
        elif s[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]:
            result += 10 ** ((len(s) - i) - 1) * (ord(s[i]) - ord('0'))
        else:
            flag = False
            break
    return is_positive * result if flag else 0


if __name__ == '__main__':
    print(str_to_int('+123'))
    print(str_to_int('-123'))
    print(str_to_int('-123a'))
