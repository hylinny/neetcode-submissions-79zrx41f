class Solution:
    def numSquares(self, n: int) -> int:
        # base case: n == 1: just return 1
        # check if perfect square: math.sqrt(value)
        # if perfect square, we recurse
        # find least number of perfect squares that sum to n
        dp = {}
        def solution(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in dp:
                return dp[n]
            output = float('inf')
            for i in range(1, n+1):
                x = math.isqrt(i)
                if x * x != i: # not a square root
                    continue
                output = min(output, 1 + solution(n-i))
            dp[n] = output
            return dp[n]
        return solution(n)
        