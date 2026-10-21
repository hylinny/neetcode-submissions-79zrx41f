class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        evenIndex = 0
        oddIndex = 1
        for num in nums:
            if num > 0:
                output[evenIndex] = num
                evenIndex += 2
            else:
                output[oddIndex] = num
                oddIndex += 2
        return output