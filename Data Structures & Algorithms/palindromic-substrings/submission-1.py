class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = {}
        def solve(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i >= j:
                return True
            if s[i] == s[j]:
                dp[(i, j)] = solve(i+1, j-1)
            else:
                dp[(i, j)] = False
            return dp[(i, j)]
        output = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if solve(i, j):
                    output += 1
        return output 