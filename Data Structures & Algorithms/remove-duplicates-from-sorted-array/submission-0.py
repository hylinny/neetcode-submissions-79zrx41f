class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        helper = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            helper.append(nums[i])
        for i in range(len(helper)):
            nums[i] = helper[i]
        return len(helper)

        