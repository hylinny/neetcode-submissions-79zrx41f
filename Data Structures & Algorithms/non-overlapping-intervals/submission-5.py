class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals = [2, 3], [4, 5], [1, 10]
        intervals.sort(key=lambda x: x[1]) # sort by end timing
        removals = 0
        interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < interval[1]:
                # overlap, skip
                removals += 1
            else:
                interval = intervals[i]
        return removals