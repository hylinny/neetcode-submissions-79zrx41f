class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # we want to sort the array. then we maintain a window of size k, 
        # and keep track of minimum nums[right] - nums[left] so far
        nums.sort()
        l = 0
        minDifference = float('inf')
        for i in range(k-1, len(nums)):
            minDifference = min(minDifference, nums[i]-nums[l])
            l += 1
        return minDifference

        