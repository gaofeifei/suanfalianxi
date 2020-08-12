"""
BOOK:python_180_zuo.pdf(程序员代码面试指南整理)
栈和队列_第1题
1	设计一个有 getMin 功能的栈（士 ★☆☆☆）
"""
from pythonds.basic.stack import Stack

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []  # 存放所有元素
        self.minStack = []  # 存放每一次压入数据时，栈中的最小值（如果压入数据的值大于栈中的最小值就不需要重复压入最小值，小于或者等于栈中最小值则需要压入）

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.minStack or self.minStack[-1] >= x:
            self.minStack.append(x)

    def pop(self):  # 移除栈顶元素时，判断是否移除栈中最小值
        """
        :rtype: void
        """
        if self.minStack[-1] == self.stack[-1]:
            del self.minStack[-1]
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

    def isEmpty(self):
            if self.stack :
                return True
            else:
                return False


if __name__ == '__main__':
    m=MinStack()
    m.push(18)
    m.push(32)
    m.push(5)
    m.push(10)
    m.push(10)
    # m.pop()
    print(m.getMin())

    # l = [3,5,66,87,1,4,78]
    # print(l[-1])
# s = Stack()
# print(s.isEmpty())
# s.push(4)
# s.push('dog')
# print(s.peek())
