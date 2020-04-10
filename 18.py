"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
思路：对于每走过一个位置都进行记录，通过参数(right, down. left. up)控制遍历数组方向(i++, j++, i--, j--)
"""


def print_matrix(test_list: list):
    walk_list = []
    if not test_list:
        return
    rows = len(test_list)
    cols = len(test_list[0])
    flag_list = []
    for _ in range(rows):
        tmp_list = [False for _ in range(cols)]
        flag_list.append(tmp_list)
    # flag_list[0][-1] = True

    direction = "right"
    i, j = 0, 0
    while not flag_list[i][j]:
        walk_list.append(test_list[i][j])
        flag_list[i][j] = True
        if direction == 'right':
            if j < cols - 1 and not flag_list[i][j+1]:  # 向右遍历时，判断右边是否经过
                j += 1
            else:
                direction = 'down'
                i += 1
        elif direction == 'down':
            if i < rows - 1 and not flag_list[i+1][j]:  # 向下遍历时，判断下边是否经过
                i += 1
            else:
                direction = 'left'
                j -= 1
        elif direction == 'left':
            if j > 0 and not flag_list[i][j-1]:     # 向左遍历时，判断边左边是否经过
                j -= 1
            else:
                direction = 'up'
                i -= 1
                print('up', i, j, test_list[i][j])
        elif direction == 'up':
            if i > 0 and not flag_list[i-1][j]:   # 向上遍历时，判断边上边是否经过
                i -= 1
            else:
                direction = "right"
                j += 1
    return walk_list


if __name__ == '__main__':
    print(print_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
