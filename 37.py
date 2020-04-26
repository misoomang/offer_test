"""
数字在排序数组中出现的次数
思路一：遍历整个数组
思路二：二分查找，若找到对应数字，遍历左右两边数字
"""


def get_number_of_k(data, k):
    if not data:
        return
    else:
        middle = len(data) // 2
        if data[middle] == k:
            count, left_middle, right_middle = 1, middle - 1, middle + 1
            while left_middle >= 0:
                if data[left_middle] == k:
                    count += 1
                left_middle -= 1
            while right_middle < len(data):
                if data[right_middle] == k:
                    count += 1
                right_middle += 1
            return count
        elif data[middle] < k:
            return get_number_of_k(data[:middle], k)
        else:
            return get_number_of_k(data[middle+1:], k)


if __name__ == '__main__':
    print(get_number_of_k([1, 2, 3, 3, 3, 3, 4, 5, 6], 3))
