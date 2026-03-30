class Solution:
    def check(self, nums: List[int]) -> bool:
        # two pass: find the first decreasing element
        pivot = -1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                pivot = i
                break
        if pivot == -1: # array already sorted
            return True
        for i in range(1, len(nums)):
            index = (pivot + i) % len(nums)
            if nums[index] < nums[index-1]:
                return False
        return True