"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
"""


def multiply(A):
    lenth = len(A)
    result = [1] * lenth
    for i in range(lenth):
        for j in range(lenth):
            if i == j:
                continue
            result[i] *= A[j]
    return result

if __name__ == '__main__':
    print(multiply([0, 1, 1]))
