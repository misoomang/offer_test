"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""


def find_nums_appear_once(array):
    num_dict = dict()
    for item in array:
        if item not in num_dict:
            num_dict[item] = 1
        else:
            num_dict[item] += 1
    result_list = [key for key, value in num_dict.items() if value == 1]
    return result_list


if __name__ == '__main__':
    print(find_nums_appear_once([1, 2, 2, 3, 3, 4, 4, 5]))
