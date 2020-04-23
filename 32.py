"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""


def compare(s1, s2):
    num1 = int(s1 + s2)
    num2 = int(s2 + s1)
    if num1 <= num2:
        return str(num1)
    else:
        return str(num2)


def print_min_number(num_list):
    if not num_list:
        return []
    elif len(num_list) == 1:
        return num_list[0]
    else:
        str_numbers_list = [str(item) for item in num_list]
        str_num = compare(str_numbers_list[0], str_numbers_list[1])
        if len(str_numbers_list) >= 3:
            for i in range(2, len(str_numbers_list)):
                str_num = compare(str_num, str_numbers_list[i])
    return int(str_num)


if __name__ == '__main__':
    print(print_min_number([3, 32, 321]))
