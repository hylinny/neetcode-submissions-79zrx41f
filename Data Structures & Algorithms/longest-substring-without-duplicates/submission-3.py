class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashset = set()
        length = 0
        maxLength = 0
        for r in range(len(s)):
            if s[r] not in hashset:
                length += 1
                hashset.add(s[r])
                maxLength = max(maxLength, length)
            else:
                while s[r] in hashset:
                    hashset.remove(s[l])
                    l += 1
                    length -= 1
                hashset.add(s[r])
                length += 1
        return maxLength
