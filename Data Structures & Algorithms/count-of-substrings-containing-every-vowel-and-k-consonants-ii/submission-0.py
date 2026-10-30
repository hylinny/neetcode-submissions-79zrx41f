class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # while shrinking left window, we can count the number of valid starting points. we only shrink if window is valid
        # initially, multiplicative factor is 0
        # when we first enter left window shrinking while loop, we initialize multiplicative factor to 1
        factor = 0
        l = 0
        vowelCount = 0
        vowelMap = {
            "a": 0,
            "e": 0,
            "i": 0,
            "o": 0,
            "u": 0
        }
        consonantCount = 0
        output = 0
        for r in range(len(word)):
            if word[r] in vowelMap:
                if vowelMap[word[r]] == 0:
                    vowelCount += 1
                vowelMap[word[r]] += 1
            else:
                consonantCount += 1
            if consonantCount > k:
                factor = 0
                while consonantCount > k:
                    if word[l] in vowelMap:
                        vowelMap[word[l]] -= 1
                        if vowelMap[word[l]] == 0:
                            vowelCount -= 1
                    else:
                        consonantCount -= 1
                    l += 1
            while l < len(word) and word[l] in vowelMap and vowelMap[word[l]] > 1:
                vowelMap[word[l]] -= 1
                l += 1
                factor += 1
            if vowelCount == 5 and consonantCount == k:
                output += (1 + factor)
        return output


