"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # bar: counting tap ins and tap outs
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        # two pointer approach
        # for every increment in start, we add count
        # for every decrement in end, we subtract count
        rooms = 0
        count = 0
        l, r = 0, 0
        while l < len(start) and r < len(end):
            if start[l] < end[r]:
                count += 1
                rooms = max(rooms, count)
                l += 1
            else:
                count -= 1
                r += 1
        return rooms
