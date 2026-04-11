class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # maintain a hashmap of t containing frequencies
        # maintain two pointers
        # if match found, move left pointer inwards until substring no longer present
        # while doing the above, update output string
        # increment matches as long as smap[c] = tmap[c]
        # decrement matches as long as smap[c] < tmap[c]
        # O, OU, OUZ, OUZOD, OUZODY, OUZODYX, 
        # UZODYX, ZODYX, ODYX, ODYXA, ODYXAZ,
        # DYXAZ, YXAZ, XAZ, XAZV
        tmap = defaultdict(int)
        for c in t:
            tmap[c] += 1
        smap = defaultdict(int)
        count = 0 # tracks matched characters so far
        match = len(tmap)
        boundary = [0, 0] # tracks substring left and right pointer
        minLength = float('inf')
        l = 0
        for r in range(len(s)):
            smap[s[r]] += 1
            if s[r] in tmap and smap[s[r]] == tmap[s[r]]:
                count += 1
            while count == match:
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    boundary = [l, r]
                smap[s[l]] -= 1
                if s[l] in tmap and smap[s[l]] < tmap[s[l]]:
                    count -= 1
                l += 1
        return s[boundary[0]:boundary[1]+1] if minLength != float('inf') else ""


            
                
