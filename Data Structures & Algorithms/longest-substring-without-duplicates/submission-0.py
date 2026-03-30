class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        hashset = set()
        left = 0
        for i in range(len(s)):
            # if current character is already found
            while s[i] in hashset:
                hashset.remove(s[left])
                left += 1
            # otherwise, add current character to hashset,
            # and update maxLength
            hashset.add(s[i])
            maxLength = max(maxLength, i - left + 1)
        return maxLength
            
