class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # sort by first element
        output = []
        for interval in intervals:
            if not output or output[-1][1] < interval[0]:
                # add interval to output
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], interval[1])
        return output
        