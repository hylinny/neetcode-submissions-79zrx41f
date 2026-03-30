class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0: -1}
        cum = 0
        # compute prefix sum on the fly
        for i in range(len(nums)):
            cum += nums[i]
            if cum % k in hashmap:
                if i - hashmap[cum % k] >= 2:
                    return True
            else:
                hashmap[cum % k] = i # store the earliest index
        return False
        # multiple of k
        # (prefixSum[i] - prefixSum[j]) % k == 0
        # rearrange: prefixSum[k] % k = prefixSum[i] % k

        # nums = [23, 2, 4, 6, 7]
        # prefix = 23, 25, 29, 35, 42
        # rem    = 5, 1, 5 (found!)
        # hashset stores remainders
        # hashset = {5, 1, }

        # nums = [1,0,1,0,1], k = 4
        # prefix=[1,1,2,2,3]
