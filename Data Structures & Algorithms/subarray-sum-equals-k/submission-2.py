class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix[i] - prefix[j] = k
        # prefix[i] - k = prefix[j]
        # check if prefix[j] is in hashmap, then add its value
        count = defaultdict(int)
        count[0] = 1
        prefixSum = 0
        output = 0
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum - k in count:
                output += count[prefixSum - k]
            count[prefixSum] += 1
        return output