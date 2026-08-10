class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        interval = intervals[0]
        output = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > interval[1]: # non-overlapping
                output.append(interval)
                interval = intervals[i]
            else: # overlapping
                interval[1] = max(interval[1], intervals[i][1])
        output.append(interval)
        return output