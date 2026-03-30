class MinStack:

    def __init__(self):
        self.stack1 = [] # original stack
        self.stack2 = [] # min value so far

    def push(self, val: int) -> None:
        self.stack1.append(val)
        minimum = float('inf')
        if self.stack2:
            minimum = self.stack2[-1]
        self.stack2.append(min(minimum, val))

    def pop(self) -> None:
        self.stack1.pop()
        self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1]
