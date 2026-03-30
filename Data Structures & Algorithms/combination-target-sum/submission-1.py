class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # recursive solution, coin change
        # choose to take current number, or not to take it
        output = []
        def solve(i, array, cum):
            if cum > target:
                return
            if i == len(nums):
                if cum == target:
                    output.append(array.copy())
                return
            array.append(nums[i])
            solve(i, array, cum + nums[i])
            array.pop()
            solve(i+1, array, cum)
        solve(0, [], 0)
        return output
            