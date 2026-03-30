class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (r - l) // 2 + l
            if target <= nums[m]:
                r = m
            elif target > nums[m]:
                l = m + 1
        return l if nums[l] == target else -1
        