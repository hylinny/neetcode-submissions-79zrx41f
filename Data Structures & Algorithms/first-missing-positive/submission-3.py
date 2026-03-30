class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # capacity of nums is n, so smallest positive integer has to be in [1, n]
        # else, return n+1
        hashset = set(nums)
        for i in range(1, len(nums)+1):
            if i not in hashset:
                return i
        return len(nums)+1
