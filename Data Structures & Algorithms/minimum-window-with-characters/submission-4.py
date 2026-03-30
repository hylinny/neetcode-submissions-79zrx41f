class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # maintain hashmap of t and s
        # maintain counter. when it hits t, we found a match.
        # increment counter when we found s in t and ++hashmap[s] == hashmap[t]
        # when we decrement to shrink left window, 
        # if hashmap[s] < hashmap[t], we can stop and continue expanding right side.
        # ensure that left always points to an element in our map
        output = ""
        length = float('inf')
        smap = defaultdict(int)
        tmap = defaultdict(int)
        for c in t:
            tmap[c] += 1
        n = len(set(t)) # unique characters in t
        counter = 0
        l = 0
        for r in range(len(s)):
            while l < r and s[l] not in tmap:
                l += 1
            # s[l] = s[r] = Z
            smap[s[r]] += 1
            if smap[s[r]] == tmap[s[r]]:
                counter += 1
            print(s[l:r+1])
            while counter == n: # substring found!
                if r - l + 1 < length:
                    length = r - l + 1
                    output = s[l:r+1]
                smap[s[l]] -= 1
                if smap[s[l]] < tmap[s[l]]:
                    counter -= 1
                l += 1
        return output

            
                
