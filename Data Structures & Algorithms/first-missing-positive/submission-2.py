class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(len(nums)):
            value = abs(nums[i]) # value to check
            if 0 <= value - 1 < len(nums):
                if nums[value-1] == 0:
                    nums[value-1] = -(len(nums)+1)
                else:
                    nums[value-1] = -abs(nums[value-1])
        
        for i in range(1, len(nums)+1):
            if nums[i-1] >= 0:
                return i
        return len(nums)+1
