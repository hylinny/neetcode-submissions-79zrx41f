class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # at day one, we can choose to buy 1 day pass, 7 day pass or 30 day pass.
        # try all of them
        # keep track of recursion using days reached, as well as remaining pass days
        dp = {}
        def solve(i, totalDays):
            if i == len(days):
                return 0
            if (i, totalDays) in dp:
                return dp[(i, totalDays)]
            # current stage, try to buy each type of pass
            bestCost = float('inf')
            if totalDays >= days[i]:
                bestCost = min(bestCost, solve(i+1, totalDays))
            else: # no more days left, need to buy new pass
                # buy each pass manually
                bestCost = min(bestCost, solve(i+1, days[i]) + costs[0]) # 1 day pass
                bestCost = min(bestCost, solve(i+1, days[i] + 6) + costs[1]) # 7 day pass
                bestCost = min(bestCost, solve(i+1, days[i] + 29) + costs[2]) # 30 day pass
            dp[(i, totalDays)] = bestCost
            return bestCost
        return solve(0, 0)

        