class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        # quickselect algorithm
        def quickselect(l, r):
            pivot = nums[l]
            left, right = l+1, r
            while left <= right:
                if nums[left] <= pivot:
                    left += 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
            # swap pivot into correct position
            nums[l], nums[right] = nums[right], nums[l]
            if right == k:
                return nums[right]
            elif right < k:
                return quickselect(right+1, r)
            else:
                return quickselect(l, right-1)
        return quickselect(0, len(nums)-1)
            