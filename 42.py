"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
思路一：遍历数组，用和数字减去后是否仍在数组中，存储结果后进行排序取第一个
思路二：低指针指向头部，高指针指向末尾，求和与S比较，如果比S大，高指针往前移动；如果比S小，低指针向后移动
"""


def find_numbers_with_sum(array, tsum):
    if not array:
        return []
    result_list = []
    for item in array:
        if tsum - item in array:
            result_list.append([item, tsum - item])

    if result_list:
        sort_list = sorted(result_list, key=lambda k: k[0] * k[1])
        return sort_list[0]
    else:
        return []


def find_numbers_with_sum_1(array, tsum):
    if not array:
        return []
    low = 0
    high = len(array) - 1
    result = [array[-1], array[-1]]
    plus_result = array[0] + array[high]
    if plus_result > tsum:
        high -= 1
    elif plus_result < tsum:
        low += 1
    else:
        if array[low] * array[high] < result[0] * result[1]:
            result[0], result[1] = array[low], array[high]
        high -= 1
        low += 1
    return result


if __name__ == '__main__':
    print(find_numbers_with_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
    print(find_numbers_with_sum_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
