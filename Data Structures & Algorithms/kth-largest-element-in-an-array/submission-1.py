class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quickselect
        # first element as pivot, partition, then quickselect either side
        # depending on location of pivot
        k = len(nums)-k
        def quickselect(l, r):
            pivot = nums[l]
            left, right = l + 1, r
            while left <= right:
                if nums[left] <= pivot:
                    left += 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
            # at this point, we want to swap pivot with right
            nums[l], nums[right] = nums[right], nums[l]
            # pivot is at index right
            if right == k:
                return nums[k]
            elif right < k:
                return quickselect(right + 1, r)
            else:
                return quickselect(l, right - 1)

        return quickselect(0, len(nums)-1)