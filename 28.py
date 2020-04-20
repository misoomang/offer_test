"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


def more_than_half_num_solution(num_list):
    if not num_list:
        return 0
    elif len(num_list) == 1:
        return num_list[0]
    else:
        half_len = len(num_list) / 2
        num_dict = {}
        for item in num_list:
            if item not in num_dict:
                num_dict[item] = 1
            else:
                num_dict[item] += 1
        new_dict = {key: value for key, value in num_dict.items() if value > half_len}
        return list(new_dict.keys()) if new_dict else 0


if __name__ == '__main__':
    print(more_than_half_num_solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
