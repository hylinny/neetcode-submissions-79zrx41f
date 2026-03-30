class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        output = 0
        for num in nums:
            if num-1 in hashset:
                continue
            curr = num
            sequence = 0
            while curr in hashset:
                curr += 1
                sequence += 1
            output = max(output, sequence)
        return output