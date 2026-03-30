class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        def recurse(x, y):
            if x == 0 or y == 0:
                return 1
            if memo[x][y] != -1:
                return memo[x][y]
            memo[x][y] = recurse(x-1, y) + recurse(x, y-1)
            return memo[x][y]
        return recurse(m-1, n-1)
