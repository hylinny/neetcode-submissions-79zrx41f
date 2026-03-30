class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= reachable:
                reachable = i
        return reachable == 0