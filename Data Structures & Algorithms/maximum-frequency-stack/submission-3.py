class FreqStack:

    def __init__(self):
        self.hashmap = defaultdict(int) # for push operations
        self.countarray = [[]] # for pop operations

    def push(self, val: int) -> None:
        self.hashmap[val] += 1
        count = self.hashmap[val]
        if count == len(self.countarray):
            self.countarray.append([])
        self.countarray[count].append(val)

    def pop(self) -> int:
        value = self.countarray[-1].pop()
        self.hashmap[value] -= 1
        if len(self.countarray[-1]) == 0:
            self.countarray.pop()
        return value

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()