class Solution:
    def myPow(self, x: float, n: int) -> float:
        # divide and conquer
        # if x is even, then x^n = x^n/2 * x^n/2
        # if x is odd, then x^n = x^n//2 * x^n//2 * x
        # base case: x = 0 return 1, x = 1 return x
        def solve(i):
            nonlocal x
            if i == 0:
                return 1
            half = solve(i // 2)
            if i % 2 == 0:
                return half * half
            else:
                return half * half * x
        result = solve(abs(n))
        if n >= 0:
            return result
        else:
            return 1 / result