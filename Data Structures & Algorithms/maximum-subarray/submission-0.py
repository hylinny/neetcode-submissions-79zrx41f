class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # track max so far
        # if values goes below zero, reset counter
        result = float('-inf')
        maxSoFar = 0
        for num in nums:
            if maxSoFar < 0:
                maxSoFar = 0
            maxSoFar += num
            result = max(maxSoFar, result)
        return result
            