#  Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. 
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = sys.maxsize     

    def push(self, x: 'int') -> 'None':
        self.stack.append(x)
        if x < self.min:
            self.min = x

    def pop(self) -> 'None':
        popped = self.stack.pop()
        if popped == self.min:
            self.min = min(self.stack) if self.stack else sys.maxsize

    def top(self) -> 'int':
        return self.stack[-1]

    def getMin(self) -> 'int':
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
