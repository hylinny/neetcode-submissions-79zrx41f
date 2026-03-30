class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x = x ^ n/2 * x ^ n/2 ( * x if n is odd)
        def solve(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            half = solve(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        ans = solve(x, abs(n))
        return ans if n > 0 else 1 / ans