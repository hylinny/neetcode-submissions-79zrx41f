class Solution:
    def trap(self, height: List[int]) -> int:
        # calculate vertical block's value
        # formula: max(min(prefix[i-1], suffix[i+1]) - height[i], 0)
        # no water can be at the edges
        suffix = [0] * len(height)
        suffix[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        prefixSum = height[0]
        area = 0
        for i in range(1, len(height)-1):
            area += max(min(prefixSum, suffix[i+1]) - height[i], 0)
            prefixSum = max(prefixSum, height[i])
        return area

        