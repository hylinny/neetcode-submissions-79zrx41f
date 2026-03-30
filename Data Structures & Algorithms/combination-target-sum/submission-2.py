class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # choose to take current (i), or skip (i+1)
        array = []
        output = []
        def solve(i, cum):
            if cum == target:
                output.append(array.copy())
                return
            if i == len(nums) or cum > target:
                return
            # choose to skip
            solve(i+1, cum)
            # choose to take
            array.append(nums[i])
            solve(i, cum + nums[i])
            array.pop()
        solve(0, 0)
        return output