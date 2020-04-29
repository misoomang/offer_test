"""
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“
红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。
现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
"""


def is_continuous(numbers):
    numbers.sort()
    jokers_num = 0
    new_numbers = list()
    for num in numbers:
        if num == 0:
            jokers_num += 1         # 获得大小王的数量
        else:
            new_numbers.append(num)

    total_diff_value = 0
    for i in range(len(new_numbers) - 1):
        diff_value = new_numbers[i + 1] - new_numbers[i]
        if diff_value == 0:     # 如果有对子
            return False
        else:
            total_diff_value += diff_value - 1      # 若相差2，用1张joker就可补足。。。
    total_diff_value -= jokers_num

    return True if total_diff_value <= 0 else False     # 相差的值和大小王数量之差


if __name__ == '__main__':
    print(is_continuous([1, 3, 0, 0, 6]))
    print(is_continuous([1, 3, 0, 0, 1]))
    print(is_continuous([1, 3, 0, 0, 5]))
