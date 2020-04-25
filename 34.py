"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""


def first_not_repeating_char(alpha):
    alpha_set = set(list(alpha))
    for i in alpha_set:
        if alpha.count(i) == 1:
            print(alpha.index(i))


def first_not_repeating_char_1(alpha):
    alpha_dict = dict()
    for i in range(len(alpha)):
        if alpha[i] not in alpha_dict:
            alpha_dict[alpha[i]] = 1
        else:
            alpha_dict[alpha[i]] += 1
    for key, value in alpha_dict.items():
        if value == 1:
            print(alpha.index(key))


if __name__ == '__main__':
    first_not_repeating_char('qweqwerty')
    first_not_repeating_char_1('qweqwerty')
