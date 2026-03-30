class Solution:
    def countSubstrings(self, s: str) -> int:
        output = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    output += 1
        return output 
                