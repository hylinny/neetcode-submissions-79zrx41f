class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first = second = 0
        output = []
        while first < len(firstList) and second < len(secondList):
            start = max(firstList[first][0], secondList[second][0])
            end = min(firstList[first][1], secondList[second][1])
            if start <= end: # valid intersection
                output.append([start, end])
            if firstList[first][1] > secondList[second][1]:
                second += 1
            else:
                first += 1
        return output