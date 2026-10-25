import bisect

class Solution:

    def __init__(self, w: list[int]):
        self.cum = [w[0]] # probability of picking index i -> random number <= self.cum[i]
        for i in range(1, len(w)):
            self.cum.append(self.cum[-1] + w[i])

    def pickIndex(self) -> int:
        number = random.randint(1, self.cum[-1])
        index = bisect.bisect_left(self.cum, number)
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()