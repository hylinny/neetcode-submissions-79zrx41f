class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n) approach
        output = [0] * len(nums)
        for i in range(len(nums)):
            index = (i + k) % len(nums)
            output[index] = nums[i]
        for i in range(len(output)):
            nums[i] = output[i]
        