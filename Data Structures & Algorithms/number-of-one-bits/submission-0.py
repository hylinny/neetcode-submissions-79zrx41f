class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for i in range(32):
            mask = 1 << i
            if mask & n:
                result += 1
        return result
        