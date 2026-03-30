class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(len(nums)):
            val = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    val = max(val, dp[j])
            dp[i] = val + 1
        return max(dp)