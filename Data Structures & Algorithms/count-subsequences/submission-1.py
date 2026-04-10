import sys
sys.setrecursionlimit(10000)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # at current i, j, if they are equal, return i+1, j+1
        # else, return sum 
        dp = {}
        def solve(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            output = 0
            if s[i] == t[j]:
                output += solve(i+1, j+1)
            output += solve(i+1, j)
            dp[(i, j)] = output
            return output
        return solve(0, 0)