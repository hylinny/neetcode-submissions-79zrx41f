class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        array = [] # for backtracking
        def solve(i):
            if i == len(nums):
                output.append(array.copy())
                return output
            # choose to skip or take
            # take
            array.append(nums[i])
            solve(i+1)
            array.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            solve(i+1)

        solve(0)
        return output