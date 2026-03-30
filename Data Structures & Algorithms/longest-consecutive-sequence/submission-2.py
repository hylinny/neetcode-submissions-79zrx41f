class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        lengthSoFar = 0
        for num in nums:
            length = 0
            if num - 1 in numset:
                continue
            curr = num
            while curr in numset:
                curr += 1
                length += 1
            lengthSoFar = max(length, lengthSoFar)
        return lengthSoFar

