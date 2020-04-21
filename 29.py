"""
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
思路一：进行排序，取前k个数
思路二：构建最小堆，遍历取k个数
"""


import math


# 快排
def make_sort_list(num_list):
    if not num_list:
        return []
    elif len(num_list) == 1:
        return [num_list[0]]
    else:
        num = num_list[0]
        return make_sort_list([i for i in num_list if i < num]) + [num] + make_sort_list([i for i in num_list if i > num])


def get_least_numbers_solution(num_list, k):
    sorted_list = make_sort_list(num_list)
    if len(sorted_list) <= k:
        return sorted_list
    else:
        return sorted_list[:k]


result = []


def get_least_numbers_solution_heap(num_list, num):
    n = len(num_list)
    for i in range(int(math.log(n, 2))):
        for j in range(n//2):       # j范围为最后一个有叶子节点的索引,代表根节点索引
            k = 2*j + 2 if 2*j + 2 < n and num_list[2*j + 2] < num_list[2*j+1] else 2*j + 1     # 根节点左右子树，获取左右子树中较小的节点索引
            if num_list[j] > num_list[k]:
                num_list[j], num_list[k] = num_list[k], num_list[j]
    if num > 0:
        num_list[0], num_list[-1] = num_list[-1], num_list[0]       # num_list[0]为根节点，为最小值
        result.append(num_list.pop())           # 将最小值加入到数组中
        num -= 1
        get_least_numbers_solution_heap(num_list, num)      # 重建最小堆


if __name__ == '__main__':
    print(get_least_numbers_solution([4, 5, 1, 6, 2, 7, 3, 8], 4))
    get_least_numbers_solution_heap([4, 5, 1, 6, 2, 7, 3, 8], 4)
    print(result)
