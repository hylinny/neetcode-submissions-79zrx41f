class Solution:
    def trap(self, height: List[int]) -> int:
        # prefix, suffix
        # obviously no water will be stored at the ends
        # iterate from 1 to len(height)-1 inclusive
        suffix = [0] * len(height)
        suffix[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        water = 0
        prefix = 0
        for i in range(1, len(height)-1):
            prefix = max(height[i-1], prefix)
            water += max(min(prefix, suffix[i+1])-height[i], 0)
        return water