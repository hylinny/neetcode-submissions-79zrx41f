class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def solve(i):
            if i in dp:
                return dp[i]
            if i == 0:
                return 1
            length = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    length = max(length, 1 + solve(j))
            dp[i] = length
            return length
        return max(solve(i) for i in range(len(nums)))

