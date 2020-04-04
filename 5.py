"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。
"""


class Queue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, number: int):
        self.stack_1.append(number)

    def pop(self):
        if not self.stack_2:                # 从stack1从后到前放入stack2中
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        if not self.stack_2:                # 若此时stack2还是空，则无法进行pop
            return 'Queue is empty'
        return self.stack_2.pop()
