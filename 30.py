"""
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
"""


def find_greatest_sum_of_sub_array(num_list):
    if not num_list:
        return []
    elif len(num_list) == 1:
        return num_list[0]
    else:
        item_dict = {}
        for j in range(1, len(num_list)):
            item_dict['{0}-{1}'.format(0, j)] = sum(num_list[: j+1])
        sort_list = sorted(item_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)        # 按照和倒叙排列

        return sort_list[0]


def find_greatest_sum_of_sub_array_1(num_list):
    new_list = [0] * (len(num_list) + 1)
    new_list[0] = num_list[0]
    max_num = num_list[0]
    for i in range(1, len(num_list)):
        if new_list[i - 1] < 0:             # 若求和以后出现负数，下一次则直接复制重新开始计算
            new_list[i] = num_list[i]
        else:
            new_list[i] = new_list[i - 1] + num_list[i]
        if new_list[i] > max_num:
            max_num = new_list[i]
    return max_num


if __name__ == '__main__':
    print(find_greatest_sum_of_sub_array([6, -3, -2, 7, -15, 1, 2, 2]))
    print(find_greatest_sum_of_sub_array_1([6, -3, -2, 7, -15, 1, 2, 2]))
