class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        maxFreq = 0
        l = 0
        output = 0
        for r in range(len(s)):
            hashmap[s[r]] += 1
            maxFreq = max(maxFreq, hashmap[s[r]])
            # print(hashmap)
            # condition violated if window size - max frequency > k
            while r - l + 1 - maxFreq > k:
                hashmap[s[l]] -= 1
                l += 1
            output = max(output, r - l + 1)
            
        return output