"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
思路：循环数组中字母，取第一个，后续组成一部分数据，第一个数据 + 后续数据进行递归的结果
"""


def full_prmutate(alpth_list):
    if len(alpth_list) == 1:
        return alpth_list[0]
    else:
        result = []
        for i in range(len(alpth_list)):
            full_list = full_prmutate(alpth_list[:i] + alpth_list[i+1:])
            for j in full_list:
                result.append(alpth_list[i] + j)
        return result


if __name__ == '__main__':
    print(full_prmutate('tkc'))