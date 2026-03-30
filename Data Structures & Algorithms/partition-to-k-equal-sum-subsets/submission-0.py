class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # backtracking
        # if our sum reaches target, backtrack with k-1
        # if k == 0: we return True
        if sum(nums) % k:
            return False
        target = sum(nums) // k
        taken = [False] * len(nums)
        def backtrack(i, k, cum):
            if k == 0:
                return True
            if cum == target:
                return backtrack(0, k-1, 0)
            for j in range(i, len(nums)):
                if taken[j] or cum + nums[j] > target:
                    continue
                taken[j] = True
                if backtrack(j+1, k, cum + nums[j]):
                    return True
                taken[j] = False
            return False
        return backtrack(0, k, 0)