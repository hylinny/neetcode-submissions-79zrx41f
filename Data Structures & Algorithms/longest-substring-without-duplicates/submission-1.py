class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0
        maxLength = 0
        for r in range(len(s)):
            if s[r] not in hashset:
                hashset.add(s[r])
                maxLength = max(maxLength, r-l+1)
            else:
                while s[r] in hashset:
                    hashset.remove(s[l])
                    l += 1
                hashset.add(s[r])
        return maxLength