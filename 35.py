"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
"""


def MergeElem(data, start, mid, end, temp):  # data[start...mid], data[mid+1...end]
    print(data, start, mid, end, temp)
    cnt = 0
    i = start
    j = mid + 1
    k = start
    while i <= mid and j <= end:            # 合并(治)
        if data[j] < data[i]:  # data[start...i...mid] data[mid+1...j...end]
            temp[k] = data[j]
            cnt += j - k
            j += 1
            k += 1
        else:
            temp[k] = data[i]
            i += 1
            k += 1

    while i <= mid:         # 合并(治)
        temp[k] = data[i]
        i += 1
        k += 1
    while j <= end:
        temp[k] = data[j]
        j += 1
        k += 1
    data[start:end+1] = temp[start:end+1]
    return cnt


def InverseCore(data, start, end, temp):
    cnt = 0
    if start < end:
        mid = (start + end) // 2
        cnt += InverseCore(data, start, mid, temp)      # 分
        cnt += InverseCore(data, mid+1, end, temp)      # 分
        cnt += MergeElem(data, start, mid, end, temp)
    return cnt


def InversePairs(data):
    # write code here
    temp = data[:]
    count = InverseCore(data, 0, len(data)-1, temp)
    return count

print(InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))
