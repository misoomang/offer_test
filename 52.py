"""
请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s is None or pattern is None:
            return False
        return self.match_re(s, pattern, 0, 0)

    def match_re(self, string, pattern, s, p):
        if s == len(string) and p == len(pattern):
            return True         # string和pattern均匹配到了最末尾

        if s < len(string) and p == len(pattern):
            return False    # pattern先到末尾，而string还没到末尾，匹配不成功

        if (s < len(string) and string[s] == pattern[p]) or (s < len(string) and pattern[p] == '.'):
            # 当string的s位置和pattern的p位置相等时，或pattern的p位置为.时，均匹配后一位
            return self.match_re(string, pattern, s+1, p+1)

        if p < len(pattern) - 1 and pattern[p+1] == '*':
            # pattern的p位置后一位是*的时候
            if (s < len(string) and string[s] == pattern[p]) or (s < len(string) and pattern[p] == '.'):
                # 同时当string的s位置和pattern的p位置相等时，或同时pattern的p位置为.时
                # string: abc, pattern: a*bc, 下一次匹配string位置s+1, pattern位置p+2
                # string: abc, pattern: a*abc, 下一次匹配pattern位置p+2
                # string: aaaabc， pattern: *abc，下一次匹配string位置s+1
                return self.match_re(string, pattern, s+1, p+2) or \
                       self.match_re(string, pattern, s, p+2) or \
                       self.match_re(string, pattern, s+1, p)
            else:
                return self.match_re(string, pattern, s, p+2)
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.match('aaa', 'a.a'))
    print(s.match('aaa', 'ab*ac*a'))
    print(s.match('aaa', 'aa.a'))
    print(s.match('aaa', 'ab*a"'))



