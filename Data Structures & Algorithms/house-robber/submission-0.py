class Solution:
    def rob(self, nums: List[int]) -> int:
        # dynamic programming
        # base case: rob either house 1 or house 2
        # recursion: rob house n-2 and n, or rob n-1 and not current
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            dp.append(max(dp[i-2] + nums[i], dp[i-1]))
        return dp[-1]
        
        