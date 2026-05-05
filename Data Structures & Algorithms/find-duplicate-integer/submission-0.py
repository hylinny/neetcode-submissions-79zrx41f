class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            index = abs(nums[i])
            val = nums[index]
            if val < 0:
                return index
            nums[index] = -val
            