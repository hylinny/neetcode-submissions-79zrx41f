class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def solution(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            if target in memo:
                return memo[target]
            ways = 0
            for num in nums:
                ways += solution(target-num)
            memo[target] = ways
            return memo[target]
        return solution(target)