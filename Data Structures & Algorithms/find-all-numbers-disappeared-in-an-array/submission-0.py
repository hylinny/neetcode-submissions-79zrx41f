class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashset = set(nums)
        output = []
        for i in range(1, len(nums)+1):
            if i not in hashset:
                output.append(i)
        return output