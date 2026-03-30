class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        l, r = 0, len(heights)-1
        while l < r:
            vol = min(heights[l], heights[r]) * (r-l)
            volume = max(vol, volume)
            if heights[l] == heights[r]:
                l += 1
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return volume