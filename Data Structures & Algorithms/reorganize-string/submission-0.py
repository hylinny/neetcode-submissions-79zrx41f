class Solution:
    def reorganizeString(self, s: str) -> str:
        # most frequent one first
        hashmap = defaultdict(int)
        maxfreq = 0
        maxc = ''
        for c in s:
            hashmap[c] += 1
            if hashmap[c] > maxfreq:
                maxfreq = hashmap[c]
                maxc = c
        if maxfreq * 2 > len(s) + 1:
            return ""
        output = [''] * len(s)
        i = 0
        while hashmap[maxc] > 0:
            output[i] = maxc
            hashmap[maxc] -= 1
            i += 2
        for c in hashmap.keys():
            while hashmap[c] > 0:
                if i >= len(s):
                    i = 1 # reset i to odd index
                output[i] = c
                hashmap[c] -= 1
                i += 2
        return ''.join(output)
            
        # cdcdcdc (5, 9) (4, 7) (3, 5) (2, 3)