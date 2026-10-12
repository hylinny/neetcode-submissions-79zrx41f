from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def solve(i):
            length = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    length = max(length, 1 + solve(j))
            return length
        return max(solve(i) for i in range(len(nums)))