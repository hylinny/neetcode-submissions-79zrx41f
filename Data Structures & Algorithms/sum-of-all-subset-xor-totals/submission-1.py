class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def solve(i, cum):
            nonlocal total
            if i == len(nums):
                total += cum
                return
            # choose to take or skip
            solve(i+1, cum ^ nums[i])
            solve(i+1, cum)
        solve(0, 0)
        return total