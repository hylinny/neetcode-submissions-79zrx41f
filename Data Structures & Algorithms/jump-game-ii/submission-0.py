class Solution:
    def jump(self, nums: List[int]) -> int:
        # backwards dp
        dp = [float('inf')] * len(nums)
        dp[-1] = 0
        for i in range(len(nums)-1, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    break
                dp[i] = min(dp[i+j] + 1, dp[i])
        return dp[0]