class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        sumSoFar = 0
        for num in nums:
            sumSoFar += num
            best = max(best, sumSoFar)
            if sumSoFar < 0:
                sumSoFar = 0
        return best