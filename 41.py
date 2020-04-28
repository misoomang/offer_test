""""
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
思路：对于一个连续正式数组，开始时求和窗口大小为2，连续往后滑动求和；窗口大小为3向后滑动。。。
"""


def find_continuous_sequence(tsum):
    num_list = [i for i in range(1, 51)]
    result_list = []

    for n in range(2, 51):
        start = 0
        end = start + n
        while end <= 50:
            if sum(num_list[start: end]) == tsum:
                result_list.append(num_list[start: end])
            start += 1
            end = start + n
    return result_list


if __name__ == '__main__':
    print(find_continuous_sequence(100))
