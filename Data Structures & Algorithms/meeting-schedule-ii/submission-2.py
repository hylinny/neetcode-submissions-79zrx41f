"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort start and end times into separate arrays
        # 2 pointers: if start[l] < end[r], we increment
        # if start[l] >= end[r], we decrement
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        output = maxSoFar = 0
        l = r = 0
        while l < len(intervals):
            if start[l] < end[r]:
                # increment counter
                maxSoFar += 1
                l += 1
            else: # end found, we decrement
                maxSoFar -= 1
                r += 1
            output = max(output, maxSoFar)
        return output