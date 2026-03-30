class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachableIndex = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= reachableIndex:
                reachableIndex = i
        return reachableIndex == 0
        