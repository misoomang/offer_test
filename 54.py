"""
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
"""


class Solution:
    def __init__(self):
        self.appeared_char = list()

    # 返回对应char
    def first_appearing_once(self):
        # write code here
        return self.appeared_char[0] if self.appeared_char else None

    def insert(self, char):
        char_list = []
        if char:
            char_list = [char]
        for item in char_list:
            if item not in self.appeared_char:
                self.appeared_char.append(item)
            else:
                self.appeared_char.pop(self.appeared_char.index(item))


if __name__ == '__main__':
    s = Solution()
    s.insert('g')
    print(s.first_appearing_once())
    s.insert('o')
    print(s.first_appearing_once())
    s.insert('o')
    print(s.first_appearing_once())
    s.insert('g')
    print(s.first_appearing_once())
    s.insert('l')
    print(s.first_appearing_once())
    s.insert('e')
    print(s.first_appearing_once())


