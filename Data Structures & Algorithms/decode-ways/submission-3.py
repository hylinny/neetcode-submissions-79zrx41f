class Solution:
    def numDecodings(self, s: str) -> int:
        # violations:
        # number is > 26
        # number starts with 0
        # dp table: contains number of ways to decode the mapping
        # up to a certain digit
        # each iteration: add current digit to the previous dp entry (
        #    having exception of digit 0
        # ),
        # or add dp[i-2] with current digit concatenated with previous
        # digit (having exception of digits >26).
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * len(s)
        dp[0] = 1
        if s[1] != '0': # 1-digit possibility
            dp[1] += 1
        if 10 <= int(s[:2]) <= 26: # 2-digit possibility
            dp[1] += 1
        for i in range(2, len(s)):
            # 1-digit possibility:
            if s[i] != '0':
                dp[i] = dp[i-1]
            # 2-digit possibility
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1] 




