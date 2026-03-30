class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        maxSoFar = 0
        for num in nums:
            if num == 1:
                maxSoFar += 1
                maxOnes = max(maxOnes, maxSoFar)
            else:
                maxSoFar = 0
        return maxOnes 