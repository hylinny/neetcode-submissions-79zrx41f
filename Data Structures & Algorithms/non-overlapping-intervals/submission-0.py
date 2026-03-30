class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # base case: index >= intervals. just return 0
        # recurrence: 
        # [1, 10], [2, 3], [4, 5], 
        dp = {}
        def solution(i, next):
            if i < 0:
                return 0
            if (i, next) in dp:
                return dp[(i, next)]
            result = solution(i-1, next) # don't take current interval i
            if next == -1 or intervals[i][1] <= intervals[next][0]:
                # if current and next interval don't collide
                # take current interval
                # remember: prev solution call is optimal
                result = max(result, 1 + solution(i-1, i))
            dp[(i, next)] = result
            return dp[(i, next)]
        maximumIntervals = solution(len(intervals)-1, -1)
        return len(intervals) - maximumIntervals
        