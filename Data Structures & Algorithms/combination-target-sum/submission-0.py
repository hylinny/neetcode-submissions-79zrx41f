class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # recursive solution: choose to take current digit, or don't and move on
        # once target reaches 0, we append the result to an output array.

        output = []

        def recurse(target, i, array):
            if target == 0:
                output.append(array.copy())
                return
            if target < 0 or i == len(nums):
                return
            array.append(nums[i])
            recurse(target-nums[i], i, array)
            array.pop()
            recurse(target, i+1, array)
            
        recurse(target, 0, [])
        return output
        