class Solution:
    def findMin(self, nums: List[int]) -> int:
        # get middle element
        # if middle < middle-1, return middle
        # elif left half sorted, recurse right
        # elif right half sorted, recurse left
        # base case: left < right, return left immediately
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]
            m = (r - l) // 2 + l
            if nums[m] <= nums[m-1]:
                return nums[m]
            elif nums[l] <= nums[m]:
                # recurse right
                l = m + 1
            else:
                r = m - 1
        