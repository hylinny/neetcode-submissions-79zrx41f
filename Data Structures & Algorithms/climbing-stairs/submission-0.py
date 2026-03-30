class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        def climb(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return climb(n-1) + climb(n-2)
        return climb(n)
        