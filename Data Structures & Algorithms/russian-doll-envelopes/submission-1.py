import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # [[2,3],[5,4],[6,7],[6,4]]
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        heights = []
        for w, h in envelopes:
            index = bisect.bisect_left(heights, h)
            if index == len(heights):
                heights.append(h)
            else:
                heights[index] = h
        return len(heights)
