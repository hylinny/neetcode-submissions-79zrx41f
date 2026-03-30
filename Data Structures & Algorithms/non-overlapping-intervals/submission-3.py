class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removals = 0
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            if prev <= intervals[i][0]: # not overlapping
                prev = intervals[i][1]
            else:
                removals += 1
        return removals
        
        
        # [1, 2], [3, 4], [1, 10]