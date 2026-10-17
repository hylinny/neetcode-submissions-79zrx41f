class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k == 0:
            return 0
        solution = 0
        product = 1
        l = 0
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k and l <= r:
                product //= nums[l]
                l += 1
            solution += r - l + 1
        return solution