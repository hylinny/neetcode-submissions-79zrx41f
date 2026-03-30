class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        l = 0
        value = 0
        for r in range(len(nums)):
            value += nums[r]
            while l <= r and value >= target:
                minLength = min(minLength, r - l + 1)
                value -= nums[l]
                l += 1
        return 0 if minLength == float('inf') else minLength
        