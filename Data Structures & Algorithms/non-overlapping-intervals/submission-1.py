class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) # sort by end
        # greedy approach
        removedIntervals = 0
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev[1]:
                # remove interval
                removedIntervals += 1
            else:
                # include current interval, set it to prev for next iteration
                prev = intervals[i]
        return removedIntervals

        