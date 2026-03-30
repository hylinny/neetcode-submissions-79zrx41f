class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct = [0] * len(nums)
        suffixProduct = [0] * len(nums)
        output = []
        prefixProduct[0] = suffixProduct[len(nums)-1] = 1
        for i in range(1, len(nums)):
            prefixProduct[i] = prefixProduct[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffixProduct[i] = suffixProduct[i+1] * nums[i+1]
        for i in range(len(nums)):
            output.append(suffixProduct[i] * prefixProduct[i])
        return output
        
        # ultimately: multiply each array's corresponding entries tgt


        