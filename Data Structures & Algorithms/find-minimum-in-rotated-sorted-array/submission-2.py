class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # visualization:
        #   /
        #  /
        # /
        #     /
        #    / 
        # check first value
        # if mid value is greater than first value, go right 
        # else if less, we go left
        if nums[0] < nums[-1]:
            return nums[0]
        firstValue = nums[0]
        left, right = 1, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] > firstValue:
                left = mid + 1
            else:
                right = mid
        return nums[right]
        