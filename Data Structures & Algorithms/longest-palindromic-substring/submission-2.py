class Solution:
    def longestPalindrome(self, s: str) -> str:
        # for each index pair, it is a palindrome if
        # they have the same letter and dp[i+1][j-1] is true
        # base case: if i == j or i > j: true
        dp = {}
        def solve(i, j):
            if i >= j:
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            if s[i] == s[j]:
                dp[(i, j)] = solve(i+1, j-1)
            else:
                dp[(i, j)] = False
            return dp[(i, j)]
        
        output = ""
        maxLength = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if solve(i, j):
                    if j - i + 1 > maxLength:
                        maxLength = j - i + 1
                        output = s[i:j+1]
        return output
        