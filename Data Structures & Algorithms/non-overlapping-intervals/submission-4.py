class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end, greedily take intervals that end earlier
        # proof by contradiction: assume we have an optimal interval set.
        # if the first interval is the earliest ending interval, we are done.
        # otherwise, we can always replace the first interval
        # with the interval that ends earliest and our solution will
        # still be optimal since newInterval.end < originalInterval.end
        intervals.sort(key=lambda x:x[1])
        output = 0
        prevInterval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prevInterval[1]:
                # we need to remove current interval
                output += 1
            else:
                prevInterval = intervals[i]
        return output
