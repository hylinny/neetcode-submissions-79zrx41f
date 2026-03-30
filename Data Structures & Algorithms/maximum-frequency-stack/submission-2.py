class FreqStack:

    def __init__(self):
        self.hashmap = defaultdict(int) # for push operations
        self.countarray = [[]] # for pop operations
        self.maxcount = 0

    def push(self, val: int) -> None:
        self.hashmap[val] += 1
        count = self.hashmap[val]
        if count == len(self.countarray):
            self.countarray.append([])
            self.maxcount += 1
        self.countarray[count].append(val)

    def pop(self) -> int:
        value = self.countarray[self.maxcount][-1]
        self.hashmap[value] -= 1
        self.countarray[self.maxcount].pop()
        if len(self.countarray[self.maxcount]) == 0:
            self.maxcount -= 1
            self.countarray.pop()
        return value

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()