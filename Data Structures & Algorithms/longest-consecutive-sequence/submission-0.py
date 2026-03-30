class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert array to hashmap
        # for each element: if its the start of a sequence,
        # we continue finding the next element until it no longer exists in the hashmap
        # then, we record down the max sequence value
        maxsequence = 0
        numset = set(nums)
        for num in nums:
            if num - 1 in numset:
                continue
            length = 1
            while num + length in numset:
                length += 1
            maxsequence = max(length, maxsequence)
        return maxsequence
                

        