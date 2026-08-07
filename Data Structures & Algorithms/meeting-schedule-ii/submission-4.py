"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals = [(0,40),(5,10),(15,20)]
        # startTimes = [0, 5, 15]
        # endTimes = [10, 20, 40]
        startTimes = [interval.start for interval in intervals]
        endTimes = [interval.end for interval in intervals]
        startTimes.sort()
        endTimes.sort()
        minimumRooms = 0
        currentRooms = 0
        j = 0
        for i in range(len(startTimes)):
            while j < len(endTimes) and endTimes[j] <= startTimes[i]:
                currentRooms -= 1
                j += 1
            currentRooms += 1
            minimumRooms = max(minimumRooms, currentRooms)
        return minimumRooms