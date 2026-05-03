class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # problem becomes longest increasing subsequence
        # [1, 1], [2, 2], [3, 10], [4, 3], [5, 4]
        envelopes.sort()
        dp = {}
        def solve(i):
            if i in dp:
                return dp[i]
            length = 1
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    length = max(length, 1 + solve(j))
            dp[i] = length
            return length
        return max(solve(i) for i in range(len(envelopes)))