class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # TLE goes crazy
        # backtracking
        # sum = nums // k (check initially if possible)
        # if cum == sum, restart backtracking with k-1
        # if k == 0, return true if cum == sum
        # if cum > sum, return false
        # keep track of visited array, since we restart with i=0
        nums.sort(reverse=True)
        if sum(nums) % k != 0:
            return False
        subsum = sum(nums) // k
        visited = [False] * len(nums)
        def solve(i, k, cum):
            if k == 0:
                return True
            if cum == subsum:
                return solve(0, k-1, 0)
            if i == len(nums) or cum > subsum:
                return False
            # each element: choose to take or skip
            # choose to take (if not already taken)
            if visited[i]:
                return solve(i+1, k, cum)
            visited[i] = True
            if solve(i+1, k, cum + nums[i]):
                return True
            visited[i] = False
            if cum == 0:
                return False
            # choose to skip
            return solve(i+1, k, cum)
        return solve(0, k, 0)