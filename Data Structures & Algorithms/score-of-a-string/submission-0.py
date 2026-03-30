class Solution:
    def scoreOfString(self, s: str) -> int:
        output = 0
        for i in range(1, len(s)):
            prev = ord(s[i-1])
            curr = ord(s[i])
            output += abs(prev - curr)
        return output