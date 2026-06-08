class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # matchsticks must be able to be
        # partitioned into 4 equal sum subsets
        # to form a square
        # partition in to k equal sum subsets problem :)
        matchsticks.sort(reverse=True)
        used = [False] * len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        subSum = total // 4
        def solve(cum, step, startIndex):
            if step == 0:
                return True
            if cum == subSum:
                return solve(0, step-1, 0)
            if cum > subSum:
                return False
            for i in range(startIndex, len(matchsticks)):
                if not used[i]:
                    used[i] = True
                    if solve(cum + matchsticks[i], step, i+1):
                        return True
                    used[i] = False
            return False
        return solve(0, 4, 0)