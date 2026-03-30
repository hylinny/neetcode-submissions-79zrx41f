class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        deltaDegree = defaultdict(int)
        for src, dst in trust:
            deltaDegree[src] -= 1
            deltaDegree[dst] += 1
        for key, value in deltaDegree.items():
            if value == n-1:
                return key
        return -1