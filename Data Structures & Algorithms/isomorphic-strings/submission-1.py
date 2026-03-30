class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for i in range(len(s)):
            if s[i] in smap and smap[s[i]] != t[i] or t[i] in tmap and tmap[t[i]] != s[i]:
                return False
            smap[s[i]] = t[i]
            tmap[t[i]] = s[i]
        return True