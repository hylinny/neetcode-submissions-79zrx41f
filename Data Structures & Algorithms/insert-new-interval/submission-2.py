class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if current interval start > newInterval end,
        # append newInterval + current interval onwards
        # if current interval end < newInterval start,
        # append current interval
        # if overlap, update newinterval start and end
        output = []
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                return output + [newInterval] + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                output.append(intervals[i])
            else: # overlap
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        output.append(newInterval)
        return output