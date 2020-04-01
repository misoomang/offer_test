"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
思路：从第一行最后一个数开始找，如果比它大，进行下一行查找；如果比它小，找其前面的数
"""


def get(arrays: list, number: int):
    rows = len(arrays) - 1
    if arrays == []:
        return False, 0, 0
    cols = len(arrays[0]) - 1

    i = 0       # 代表当前行
    j = cols    # 代表当前列
    while i <= rows and j >= 0:
        if arrays[i][j] == number:
            return True, i, j
        elif arrays[i][j] > number:
            j -= 1
        elif arrays[i][j] < number:
            i += 1
        else:
            return False, 0, 0


if __name__ == '__main__':
    find_num = 9
    array_list = [
        [1, 2, 3, 4, ],
        [5, 6, 7, 8, ],
        [9, 10, 11, 12, ],
        [13, 14, 15, 16, ],
    ]
    flag, m, n = get(array_list, find_num)
    if flag:
        print('{0}在二维数组第{1}行第{2}列'.format(find_num, m+1, n+1))
    else:
        print('没有')
