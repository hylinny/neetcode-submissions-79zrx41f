class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # stores indices of untracked values 
        output = [0] * len(temperatures)
        stack.append(0)
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prevIndex = stack.pop()
                output[prevIndex] = i - prevIndex
            stack.append(i) # append current temperature for future checking
            # note that last element in output will always be 0
            
        return output