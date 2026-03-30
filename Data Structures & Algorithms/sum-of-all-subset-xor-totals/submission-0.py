class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def solve(i, cum):
            if i == len(nums):
                return cum
            # choose to take or skip
            value = solve(i+1, cum ^ nums[i])
            value += solve(i+1, cum)
            return value
        return solve(0, 0)