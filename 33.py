"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""


def get_ugly_number_solution(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        i = 2
        ugly_lists = [1]
        while len(ugly_lists) <= index - 1:
            if i / 2 in ugly_lists or i / 3 in ugly_lists or i / 5 in ugly_lists:
                if i not in ugly_lists:
                    ugly_lists.append(i)
            i += 1
        return ugly_lists[-1]


def get_ugly_number_solution_1(index):
    if index <= 1:
        return index
    ugly_list = [1] * index
    p2, p3, p5 = 0, 0, 0
    for i in range(1, index):
        ugly_list[i] = min(ugly_list[p2] * 2, ugly_list[p3] * 3, ugly_list[p5] * 5)
        if ugly_list[i] == ugly_list[p2] * 2:
            p2 += 1
        if ugly_list[i] == ugly_list[p3] * 3:
            p3 += 1
        if ugly_list[i] == ugly_list[p5] * 5:
            p5 += 1
        print(ugly_list, p2, p3, p5)
    return ugly_list[-1]


if __name__ == '__main__':
    print(get_ugly_number_solution(10))
    print(get_ugly_number_solution_1(10))
