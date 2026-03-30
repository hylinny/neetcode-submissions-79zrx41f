class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # base case: if index >= len(nums), return True
        # recurrence: check current jump length, and 
        # loop through jump length into the future
        def solve(i):
            if i >= len(nums)-1:
                return True
            current = nums[i]
            isValid = False
            for jump in range(1, current+1):
                isValid = isValid or solve(i+jump)
            return isValid
        return solve(0)
        