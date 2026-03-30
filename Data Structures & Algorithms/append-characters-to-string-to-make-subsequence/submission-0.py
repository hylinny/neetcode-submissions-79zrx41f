class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_i = 0
        for i in range(len(s)):
            if t[t_i] == s[i]:
                t_i += 1
            if t_i == len(t):
                return 0
        return len(t) - t_i
