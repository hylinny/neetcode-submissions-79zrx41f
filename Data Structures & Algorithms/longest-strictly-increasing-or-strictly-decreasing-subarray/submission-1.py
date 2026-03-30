class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxLength = 1
        lengthSoFar = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                lengthSoFar += 1
                maxLength = max(maxLength, lengthSoFar)
            else:
                lengthSoFar = 1
        lengthSoFar = 1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > nums[i+1]:
                lengthSoFar += 1
                maxLength = max(maxLength, lengthSoFar)
            else:
                lengthSoFar = 1
        return maxLength