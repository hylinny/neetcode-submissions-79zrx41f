class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # if current sum - k is already in prefixMap, add it
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        cum = 0
        solution = 0
        for num in nums:
            cum += num
            if cum - k in prefixSum:
                solution += prefixSum[cum - k]
            prefixSum[cum] += 1
        return solution


# {
#     0 -> 1
#     2 -> 2
#     1 -> 1
#     4 -> 1
# }
