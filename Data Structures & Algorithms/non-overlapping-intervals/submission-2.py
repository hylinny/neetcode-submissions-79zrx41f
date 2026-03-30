class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # dp approach:
        # sort intervals by start time
        # choose to skip current interval, or take if it doesn't overlap with prev
        dp = {}
        def solve(i, prev):
            if i == len(intervals):
                return 0
            if (i, prev) in dp:
                return dp[(i, prev)]
            # skip interval
            skip = 1 + solve(i+1, prev)
            # take interval
            if prev != -1 and intervals[prev][1] > intervals[i][0]: 
                # there is overlap
                dp[(i, prev)] = skip
            else:
                dp[(i, prev)] =  min(skip, solve(i+1, i))
            return dp[(i, prev)]
        return solve(0, -1)
        
        
        # [1, 2], [3, 4], [1, 10]