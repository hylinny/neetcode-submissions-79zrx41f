class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums)+1)
        def solve(i):
            if dp[i] != -1:
                return dp[i]
            if i == len(nums)-1:
                return 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + solve(j))
            return max(1, dp[i])
        return max(solve(i) for i in range(len(nums)))
