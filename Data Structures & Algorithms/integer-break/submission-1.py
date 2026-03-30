class Solution:
    def integerBreak(self, n: int) -> int:
        # if n == 3, split into 2*1=2
        # if n == 2, split into 1*1=1
        if n < 4:
            return n-1
        output = 3 ** (n//3) # 14, 14//3=4, 3**4 (split into 3 4 times, deal with remainder 2 later)
        if n % 3 == 1: # if remainder == 1, we change 1*3 into 2*2
            output = (output // 3) * 4
        # deal with remainders 0 and 2
        # if 2, just multiply in, else do nothing
        return output * max(1, n%3)
        