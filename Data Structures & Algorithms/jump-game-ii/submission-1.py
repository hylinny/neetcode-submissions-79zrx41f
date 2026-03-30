class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        jumps = 0
        while r < len(nums) - 1:
            reachable = 0
            for i in range(l, r+1):
                reachable = max(reachable, nums[i] + i)
            l = r + 1
            r = reachable
            jumps += 1
        return jumps