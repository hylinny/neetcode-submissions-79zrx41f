class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[-1] = True
        for i in range(len(s)):
            for word in wordDict:
                if i + 1 - len(word) < 0:
                    continue
                if dp[i-len(word)] == True and s[i+1-len(word):i+1] == word:
                    dp[i] = True
        return dp[-2]
        