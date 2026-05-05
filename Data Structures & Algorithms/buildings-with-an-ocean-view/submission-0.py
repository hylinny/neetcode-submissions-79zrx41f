class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxheight = 0
        output = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > maxheight:
                output.append(i)
            maxheight = max(maxheight, heights[i])
        output.reverse()
        return output