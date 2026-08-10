class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        interval = intervals[0]
        removals = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= interval[1]:
                interval = intervals[i]
            else:
                removals += 1
        return removals