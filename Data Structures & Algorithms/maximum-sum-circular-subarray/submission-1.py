class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = nums[0]
        minSumSoFar = 0
        maxSumSoFar = 0
        total = 0
        for i in range(len(nums)):
            maxSumSoFar = max(nums[i], maxSumSoFar + nums[i])
            maxSum = max(maxSum, maxSumSoFar)
            minSumSoFar = min(nums[i], minSumSoFar + nums[i])
            minSum = min(minSum, minSumSoFar)
            total += nums[i]
        return max(maxSum, total - minSum) if total != minSum else maxSum
