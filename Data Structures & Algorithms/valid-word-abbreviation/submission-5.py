class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # non-adjacent, non-empty
        pointer = 0
        i = j = 0
        while i < len(abbr) and j < len(word):
            if not abbr[i].isalpha():
                if abbr[i] == '0':
                    return False
                right = i
                while not abbr[right].isalpha():
                    right += 1
                    if right >= len(abbr):
                        break
                number = int(abbr[i:right])
                j += number
                if number == 0 or j > len(word):
                    return False
                i = right
            else:
                if abbr[i] != word[j]:
                    return False
                j += 1
                i += 1
        return i == len(abbr) and j == len(word)

        