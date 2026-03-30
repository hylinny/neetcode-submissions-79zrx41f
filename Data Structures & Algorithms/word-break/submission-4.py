class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # do a for loop from i to end of s
        # if a substring detected, return true
        # if recursive call returns true
        # otherwise we can keep checking
        wordSet = set(wordDict)
        dp = {}
        def solve(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                return True
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    if solve(j+1):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        return solve(0)