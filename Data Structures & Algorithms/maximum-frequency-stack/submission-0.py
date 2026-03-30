class FreqStack:

    def __init__(self):
        self.pq = []
        self.hashmap = defaultdict(int)
        self.index = 0

    def push(self, val: int) -> None:
        self.hashmap[val] += 1
        heapq.heappush(self.pq, (-self.hashmap[val], -self.index, val)) # (frequency, insertion time, value)
        self.index += 1

    def pop(self) -> int:
        frequency, i, value = heapq.heappop(self.pq)
        self.hashmap[value] -= 1
        return value
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()