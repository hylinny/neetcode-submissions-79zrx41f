class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numset = set(nums)
        for i in range(len(nums)):
            if i+1 not in numset:
                return i+1
        return len(nums)+1
