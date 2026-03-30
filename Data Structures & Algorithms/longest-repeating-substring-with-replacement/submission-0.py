class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        # for each character iterate through string
        characters = set(s)
        # count number of characters so far.
        # if number of characters + k exceeds window size, 
        # we shrink from left side
        # otherwise, keep increasing and updating maxLength.
        for c in characters:
            left = 0
            charactercount = 0
            for i in range(len(s)):
                if s[i] == c:
                    charactercount += 1
                while charactercount + k < i - left + 1:
                    if s[left] == c:
                        charactercount -= 1
                    left += 1
                maxLength = max(maxLength, i - left + 1)
        return maxLength
