class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target is less than right element:
        # its in the right half of the sort
        # else, its in the left half
        l, r = 0, len(nums) - 1
        # if nums[mid] > left,
        # recurse right if target < left or > nums[mid]
        # elif nums[mid] < left:
        # recurse right if target < nums[mid] or target > left
        f = nums[0]
        while l < r:
            m = (r-l)//2+l
            if nums[m] == target:
                return m
            if nums[m] >= f:
                if target < f or target > nums[m]: # target right side
                    l = m+1
                else:
                    r=m
            else: # nums[m] < l
                if target < nums[m] or target >= f:
                    r=m
                else:
                    l=m+1
        return l if nums[l] == target else -1

            

