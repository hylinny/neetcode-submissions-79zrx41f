class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
                continue
            product = product * num
        if zeroes > 1:
            return [0] * len(nums)
        elif zeroes == 1:
            output = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] == 0:
                    output[i] = product
                    return output
        else: # zeroes == 0
            output = []
            for num in nums:
                output.append(product // num)
            return output