class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = [0] * 501
        for c in arr:
            count[c] += 1
        for i in range(len(count)-1, 0, -1):
            if count[i] == i:
                return i
        return -1
        