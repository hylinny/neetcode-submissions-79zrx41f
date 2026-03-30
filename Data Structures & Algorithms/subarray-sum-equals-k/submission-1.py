class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # compute prefix sum of array and store in hashmap
        # prefixSum[j] - prefixSum[i] = k
        # rearranging: prefixSum[j] - k = prefixSum[i]
        # j is current prefix sum, i is summed prefixes so far in hashmap
        prefixCount = {0: 1}
        prefixSum = 0
        output = 0
        for num in nums:
            prefixSum += num
            if prefixSum - k in prefixCount:
                output += prefixCount[prefixSum - k]
            prefixCount[prefixSum] = prefixCount.get(prefixSum, 0) + 1
        return output

        