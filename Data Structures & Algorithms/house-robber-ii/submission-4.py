class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        def solve(i, j):
            dp = [0] * (j - i + 1)
            dp[0] = nums[i]
            dp[1] = max(nums[i], nums[i+1])
            for k in range(2, len(dp)):
                dp[k] = max(dp[k-1], dp[k-2] + nums[i+k])
            return dp[-1]
        return max(solve(0, len(nums)-2), solve(1, len(nums)-1))