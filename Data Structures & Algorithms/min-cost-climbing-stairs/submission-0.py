class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def solution(step):
            if step == 0:
                return cost[0]
            if step == 1:
                return cost[1]
            if step in memo:
                return memo[step]
            memo[step] = cost[step] + min(solution(step-2), solution(step-1))
            return memo[step]
        return min(solution(len(cost)-2), solution(len(cost)-1))
        
        