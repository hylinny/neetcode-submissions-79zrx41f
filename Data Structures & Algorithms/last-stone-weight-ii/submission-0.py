class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # try to split the pile of stones as evenly as possible
        # then, we can just combine them tgt to get the min weight
        # problem is automatically solved once we achieve the first pt
        stoneSum = sum(stones)
        target = math.ceil(stoneSum/2)
        dp = [[-1] * stoneSum for _ in range(len(stones))]
        def solution(i, weight):
            if weight >= target or i >= len(stones):
                # base case reached: we can no longer further optimise
                # weight, or we reached the end of the array
                # we return the difference i.e. the "minweight" solution
                return abs(weight - (stoneSum - weight))
            if dp[i][weight] != -1:
                return dp[i][weight]
            dp[i][weight] = min(solution(i+1, weight), solution(i+1, weight+stones[i]))
            return dp[i][weight]
        return solution(0, 0)