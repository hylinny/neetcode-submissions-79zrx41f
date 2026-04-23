class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        # if current height < top of stack, we can't extend it further
        # so we try popping until condition is violated
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                # prev height's max ends here
                # so we compute its rectangle 
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, heights[i]))

        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - index))
        
        return maxArea


        