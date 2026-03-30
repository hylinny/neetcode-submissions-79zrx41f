class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        p = 0
        for c in t:
            if s[p] == c:
                p += 1
            if p == len(s):
                return True
        return p == len(s)