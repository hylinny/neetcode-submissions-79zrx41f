from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # use binary search to solve question
        output = []
        for i in range(len(nums)):
            if i == 0 or nums[i] > output[-1]:
                output.append(nums[i])
            else:
                index = bisect_left(output, nums[i])
                output[index] = nums[i]
        return len(output)
