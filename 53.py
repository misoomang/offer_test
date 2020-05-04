"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""


class Solution:
    # s字符串
    @staticmethod
    def is_numeric(s):
        if not s:
            return
        has_e = False               # 目前是否有e，若有e则不能出现在最末尾，且不能出现两个e
        has_positive = False        # 目前有+，-,没有e的时候只能出现在开头，有多个+，-只能出现在e的前面
        has_point = False           # 目前是否含有.

        for i in range(len(s)):
            if s[i].lower() == 'e':
                if i == len(s) - 1:     # e不能出现在最后一个
                    return False
                if has_e:
                    return False
                has_e = True
            elif s[i] in ('+', '-'):
                if has_positive and s[i-1].lower() != 'e':      # 已经有+，-号了，但再次出现正负号的前面不是e
                    return False
                if not has_positive:                            # 匹配+，-号之未出现+，-号
                    if i > 0 and s[i-1].lower() != 'e':        # 除去第1位出现+，-
                        return False
                has_positive = True
            elif s[i] == '.':
                if has_e:           # .出现在e之后
                    return False
                if has_point:       # 出现了多次.
                    return False
                has_point = True
            elif s[i] not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.is_numeric('+100'))
    print(s.is_numeric('5e2'))
    print(s.is_numeric('-123'))
    print(s.is_numeric('3.1416'))
    print(s.is_numeric('-1E-16'))

    print(s.is_numeric('12e'))
    print(s.is_numeric('1a3.14'))
    print(s.is_numeric('1.2.3'))
    print(s.is_numeric('+-5'))
    print(s.is_numeric('12e+4.3'))
