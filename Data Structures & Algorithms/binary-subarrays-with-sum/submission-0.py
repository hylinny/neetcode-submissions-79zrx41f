class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        cum = 0
        solution = 0
        for num in nums:
            cum += num
            if cum - goal in prefixSum:
                solution += prefixSum[cum - goal]
            prefixSum[cum] += 1
        return solution