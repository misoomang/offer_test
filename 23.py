"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。
假设输入的数组的任意两个数字都互不相同。
后序遍历顺序：左右根节点，如[4, 8, 6, 12, 16, 14, 10]中10为根节点
二叉搜索树：根节点比左节点大，比右节点小，即 左节点 < 根节点 < 右节点
思路：
如后续遍历数组[4, 8, 6, 12, 16, 14, 10]，10作为根节点，分为两部分[4, 8, 6]和[12, 16, 14]
要满足左部分小于根节点，右部分大于根节点；
对于左右部分循环此方式进行
"""


def verify_squence_of_bst(houxu_list):
    if len(houxu_list) <= 1:
        return True
    root_num = houxu_list[-1]
    i = None
    for i in range(len(houxu_list) - 1):
        if houxu_list[i] > root_num:
            break               # 获取前半部分位置
    if i is not None:
        for j in range(i, len(houxu_list) - 1):
            if houxu_list[j] < root_num:        # 出现后半部分比根节点大，则不满足该条件
                return False
    return verify_squence_of_bst(houxu_list[:i]) and verify_squence_of_bst(houxu_list[i:-1])


if __name__ == '__main__':
    list1 = [4, 8, 6, 12, 16, 14, 10]
    print(verify_squence_of_bst(list1))

    list2 = [9, 7, 8, 6, 12, 16, 14, 10]
    print(verify_squence_of_bst(list2))

    list3 = [7, 9, 8, 6, 12, 16, 14, 10]
    print(verify_squence_of_bst(list3))
