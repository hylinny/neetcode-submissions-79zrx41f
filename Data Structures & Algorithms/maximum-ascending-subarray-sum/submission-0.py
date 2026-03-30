class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # subarray
        maxSum = nums[0]
        sums = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                sums += nums[i]
                maxSum = max(maxSum, sums)
            else:
                sums = nums[i]
        return maxSum