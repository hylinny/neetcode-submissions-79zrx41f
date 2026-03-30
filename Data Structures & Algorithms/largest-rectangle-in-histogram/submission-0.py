class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force solution
        prefix = [0] * len(heights)
        stack = [0]
        for i in range(1, len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                prefix[i] = stack[-1] + 1
            stack.append(i)
        
        print(prefix)

        suffix = [len(heights)-1] * len(heights)
        stack = [len(heights)-1]
        for i in range(len(heights)-2,-1,-1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                suffix[i] = stack[-1] - 1
            stack.append(i)
        
        print(suffix)

        maxArea = 0
        for i in range(len(heights)):
            maxArea = max(maxArea, (heights[i] * (suffix[i] - prefix[i] + 1)))

        return maxArea

        


        