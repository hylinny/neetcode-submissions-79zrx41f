class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # constraints: indices must be distinct, 
        # no duplicate quadruplets
        nums.sort()
        output = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    # j > i to prevent skipping legitimate duplicates
                    continue
                l, r = j + 1, len(nums)-1
                while l < r:
                    value = nums[i] + nums[j] + nums[l] + nums[r]
                    if value > target:
                        r -= 1
                    elif value < target:
                        l += 1
                    else: # solution found
                        output.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        # skip over duplicates
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
        return output

