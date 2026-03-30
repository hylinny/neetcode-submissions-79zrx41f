class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # maintain output array
        # if current interval's end <= next interval's start, there is an overlap
        # we merge and maintain a current interval window
        output = []
        intervals.sort()
        currentInterval = intervals[0]
        for i in range(1, len(intervals)):
            if currentInterval[1] < intervals[i][0]:
                # no overlap
                output.append(currentInterval)
                currentInterval = intervals[i]
            else:
                currentInterval[0] = min(currentInterval[0], intervals[i][0])
                currentInterval[1] = max(currentInterval[1], intervals[i][1])
                # atp, currentInterval has not been appended yet

        output.append(currentInterval) # append for last iteration
        return output