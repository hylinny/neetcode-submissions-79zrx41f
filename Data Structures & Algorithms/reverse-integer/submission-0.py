class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        isNegative = False
        threshold = 2 ** 31 - 1
        if x < 0:
            isNegative = True
            x = -x
        while x > 0:
            if ans * 10 > threshold:
                return 0
            ans *= 10
            ans += x % 10
            x //= 10
        return -ans if isNegative else ans