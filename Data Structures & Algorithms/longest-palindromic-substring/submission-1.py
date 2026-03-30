class Solution:
    def longestPalindrome(self, s: str) -> str:

        dp = {}
        def solve(i, j): # check for palindrome
            if i >= j:
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            if s[i] == s[j]:
                dp[(i, j)] = solve(i+1, j-1)
            else:
                dp[(i, j)] = False
            return dp[(i, j)]
        
        length = 0
        string = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if solve(i, j):
                    if j-i+1 > length:
                        length = j-i+1
                        string = s[i:j+1]
        return string
