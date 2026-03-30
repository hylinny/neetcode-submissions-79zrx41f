class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # choose to take or include current integer
        output = []
        array = []
        def solve(i):
            if i == len(nums):
                output.append(array.copy())
                return
            solve(i+1)
            array.append(nums[i])
            solve(i+1)
            array.pop()
        solve(0)
        return output