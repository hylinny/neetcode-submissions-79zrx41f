class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newInterval = intervals[0]
        output = []
        for i in range(1, len(intervals)):
            if newInterval[1] < intervals[i][0]:
                # no overlap
                output.append(newInterval)
                newInterval = intervals[i]
            else:
                newInterval[1] = max(intervals[i][1], newInterval[1])
        output.append(newInterval)
        return output
