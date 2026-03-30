class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # number of different ways to add/subtract each number
        # all numbers must be used
        memo = {}
        def solve(i, target):
            # note that target can either be +ve or -ve during recursion
            if i == len(nums):
                return 1 if target == 0 else 0
            if (i, target) in memo:
                return memo[(i, target)]
            memo[(i, target)] = solve(i+1, target - nums[i]) + solve(i+1, target + nums[i])
            return memo[(i, target)]
        return solve(0, target)
