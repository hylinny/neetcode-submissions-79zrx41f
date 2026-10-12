import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        array = []
        for num in nums:
            index = bisect.bisect_left(array, num)
            if index == len(array):
                array.append(num)
            else:
                array[index] = num
        return len(array)