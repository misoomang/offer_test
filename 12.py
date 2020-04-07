"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
[4, 3, 6, 7, 8, 10, 2, 1, 5]     [3, 7, 1, 5, 4, 6, 8, 10, 2]
"""


def re_order_list(test_list: list):
    i_list = []     # 奇数list
    j_list = []     # 偶数list
    for i in test_list:
        if i % 2 == 1:
            i_list.append(i)
        else:
            j_list.append(i)
    i_list.extend(j_list)
    return i_list


if __name__ == '__main__':
    print(re_order_list([4, 3, 6, 7, 8, 10, 2, 1, 5]))

