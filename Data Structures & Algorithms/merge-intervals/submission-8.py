class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        prevInterval = intervals[0]
        for i in range(1, len(intervals)):
            currInterval = intervals[i]
            if currInterval[0] <= prevInterval[1]:
                prevInterval[1] = max(prevInterval[1], currInterval[1])
            else:
                output.append(prevInterval)
                prevInterval = intervals[i]
        output.append(prevInterval)
        return output



