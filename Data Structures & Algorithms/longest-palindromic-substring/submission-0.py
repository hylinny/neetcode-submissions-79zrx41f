class Solution:
    def longestPalindrome(self, s: str) -> str:
        # iterate along each character
        # then, expand leftwards and rightwards
        n = len(s)
        maxLength = 0
        maxPalindrome = ""
        for i in range(len(s)):
            # odd palindrome check
            oddLength = 1
            left, right = i-1, i+1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    oddLength += 2
                else:
                    break
                left -= 1
                right += 1
            if oddLength > maxLength:
                maxLength = oddLength
                maxPalindrome = s[left+1:right]
            # even palindrome check
            evenLength = 0
            left, right = i, i+1
            while left >= 0 and right < n:
                if s[left] == s[right]:
                    evenLength += 2
                else:
                    break
                left -= 1
                right += 1
            if evenLength > maxLength:
                maxLength = evenLength
                maxPalindrome = s[left+1:right]
        return maxPalindrome