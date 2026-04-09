class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if target == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        # ensures next l we find is unique
                        l += 1
                elif target > 0:
                    r -= 1
                else:
                    l += 1
        return output