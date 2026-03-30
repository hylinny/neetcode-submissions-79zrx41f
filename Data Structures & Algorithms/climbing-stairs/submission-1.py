class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        memo = [0] * (n+1)
        def climb(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            value = climb(n-1) + climb(n-2)
            memo[n] = value
            return value
        return climb(n)
        