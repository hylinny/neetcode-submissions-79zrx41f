import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # in place quick sort, 3 way partition
        # invariant: sort between left and right
        # if left == right, return
        def quicksort(l, r):
            if l >= r:
                return
            pivotIndex = random.randint(l, r)
            nums[pivotIndex], nums[l] = nums[l], nums[pivotIndex]
            pivot = nums[l]
            left = l + 1 
            right = r
            trackLeft = l + 1
            while left <= right:
                if nums[left] < pivot:
                    nums[left], nums[trackLeft] = nums[trackLeft], nums[left]
                    left += 1
                    trackLeft += 1
                elif nums[left] == pivot:
                    left += 1
                else: # nums[left] > pivot
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
            # swap pivot with right pointer
            nums[l], nums[trackLeft-1] = nums[trackLeft-1], nums[l]
            quicksort(l, trackLeft-2)
            quicksort(right+1, r)
        quicksort(0, len(nums)-1)
        return nums
