class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelset = {'a', 'e', 'i', 'o', 'u'}
        vowels = maxVowels = 0
        l = 0
        for r in range(len(s)):
            if r - l == k:
                if s[l] in vowelset:
                    vowels -= 1
                l += 1
            if s[r] in vowelset:
                vowels += 1
                maxVowels = max(maxVowels, vowels)
        return maxVowels
