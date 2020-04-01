"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


def replace(s: str):
    string_lenth = len(s)

    blank_num = 0
    for i in s:
        if i == ' ':    # 统计空格数量
            blank_num += 1

    new_string_lenth = string_lenth + 2 * blank_num     # 替换后的字符串长度
    new_string = [' '] * new_string_lenth                  # 初始化新字符串

    m = 0
    for n in range(string_lenth):
        if s[n] != ' ':
            new_string[m] = s[n]
            m += 1
        else:
            new_string[m] = '%'
            new_string[m+1] = '2'
            new_string[m+2] = '0'
            m += 3
    return ''.join(new_string)


if __name__ == '__main__':
    print(replace('We Are Happy'))
    print('We Are Happy'.replace(' ', '%20'))
