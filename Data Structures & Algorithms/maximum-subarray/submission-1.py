class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # compute count so far
        # if count ever goes negative, we can never have a good subarray sum by including the current element
        # so we just reset to 0 and try again for the next element.
        maxSum = float('-inf')
        sumSoFar = 0
        for num in nums:
            sumSoFar += num
            maxSum = max(maxSum, sumSoFar)
            if sumSoFar < 0:
                sumSoFar = 0
        return maxSum