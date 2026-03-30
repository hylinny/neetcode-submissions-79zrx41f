class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # either left half sorted, or right half sorted
        l, r = 0, len(nums)-1
        while l <= r:
            m = (r - l) // 2 + l
            if nums[m] == target:
                return True
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                continue
            if nums[l] <= nums[m]: # left half sorted
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # right half sorted
                if nums[m] <= nums[r]:
                    if nums[m] <= target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
        return False
        # [3, 1, 2, 3, 3, 3, 3]
        # l = 3, m = 3, r = 3
