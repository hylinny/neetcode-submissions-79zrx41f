class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # pop balloons last
        nums.insert(0, 1)
        nums.append(1)
        dp = {}
        def solve(l, r):
            if (l, r) in dp:
                return dp[(l, r)]
            if l + 1 == r:
                return 0
            maxCoins = 0
            for i in range(l+1, r):
                current = nums[l] * nums[i] * nums[r]
                current += solve(l, i) + solve(i, r)
                maxCoins = max(maxCoins, current)
            dp[(l, r)] = maxCoins
            return maxCoins
        return solve(0, len(nums)-1)
