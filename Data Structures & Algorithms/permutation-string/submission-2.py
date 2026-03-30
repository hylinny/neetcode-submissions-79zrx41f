class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        s1set = set(s1)
        s1map = {}
        s2map = {}
        for i in range(len(s1)):
            s1map[s1[i]] = s1map.get(s1[i], 0) + 1
            if s2[i] in s1set:
                s2map[s2[i]] = s2map.get(s2[i], 0) + 1
        for r in range(len(s1), len(s2)):
            if s1map == s2map:
                return True
            if s2[l] in s1set:
                s2map[s2[l]] -= 1
            if s2[r] in s1set:
                s2map[s2[r]] = s2map.get(s2[r], 0) + 1
            l += 1
        return s1map == s2map
        