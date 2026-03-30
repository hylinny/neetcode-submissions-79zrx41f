class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefixSum[i] - prefixSum[j] = k
        # prefixSum[i] - k = prefixSum[j]
        # nums = [2, 1, 2, 4]
        # hashmap -> prefixSum : count. initially, 0:1
        # {0: 1, 1: 1, 2: 2, 4: 1}
        hashmap = defaultdict(int)
        hashmap[0] = 1
        prefixSum = 0
        output = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum - k in hashmap:
                output += hashmap[prefixSum - k]
            hashmap[prefixSum] += 1
        return output