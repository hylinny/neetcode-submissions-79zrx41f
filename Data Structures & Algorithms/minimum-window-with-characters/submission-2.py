class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount, scount = {}, {}
        # sliding window approach
        for c in t:
            tcount[c] = 1 + tcount.get(c, 0)
        
        l = 0
        have, need = 0, len(tcount)
        result = [-1, -1]
        resultLength = float('inf')
        for r in range(len(s)):
            if s[r] in tcount:
                scount[s[r]] = 1 + scount.get(s[r], 0)
                if scount[s[r]] == tcount[s[r]]:
                    have += 1
            while have == need:
                # update max
                if r - l + 1 < resultLength:
                    result = [l, r]
                    resultLength = r - l + 1
                # move left pointer rightwards
                if s[l] in tcount:
                    scount[s[l]] -= 1
                    if scount[s[l]] < tcount[s[l]]:
                        have -= 1
                l += 1
        return s[result[0]:result[1]+1] if resultLength != float('inf') else ""

        


        