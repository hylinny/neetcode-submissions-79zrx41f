class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # sort nums
        # in each loop, iterate through all used and try to take
        # if curr element is free and prev element is duplicate and also free, skip
        # else take and move on
        nums.sort()
        output = []
        used = [False] * len(nums)
        def solve(path):
            if len(path) == len(nums):
                output.append(path.copy())
                return
            for i in range(len(used)):
                if not used[i] and (i == 0 or nums[i-1] != nums[i] or nums[i-1] == nums[i] and used[i-1]):
                    used[i] = True
                    path.append(nums[i])
                    solve(path)
                    path.pop()
                    used[i] = False
        solve([])
        return output