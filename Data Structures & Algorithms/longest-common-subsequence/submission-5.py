from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def solve(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + solve(i+1, j+1)
            else:
                return max(solve(i, j+1), solve(i+1, j))
        return solve(0, 0)