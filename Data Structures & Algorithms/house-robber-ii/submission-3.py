class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        # if we rob the first house, we cannot rob the last one
        # if we rob the last house, we cannot rob the first one
        dp1 = [0] * (len(nums)-1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])

        dp2 = [0] * (len(nums)-1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[2], nums[1])
        for i in range(3, len(nums)):
            dp2[i-1] = max(dp2[i-3]+nums[i], dp2[i-2])
        return max(dp1[-1], dp2[-1])
