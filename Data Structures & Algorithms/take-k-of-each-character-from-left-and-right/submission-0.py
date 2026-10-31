class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # maximum window substring
        characterMap = {
            'a': -k,
            'b': -k,
            'c': -k
        }
        for c in s:
            characterMap[c] += 1
        if characterMap['a'] < 0 or characterMap['b'] < 0 or characterMap['c'] < 0:
            return -1
        maxWindow = 0
        l = 0
        rollingMap = defaultdict(int)
        matchesFound = 0 # if this is 3, then all are found
        for r in range(len(s)):
            rollingMap[s[r]] += 1
            while rollingMap['a'] > characterMap['a'] or rollingMap['b'] > characterMap['b'] or rollingMap['c'] > characterMap['c']:
                rollingMap[s[l]] -= 1
                l += 1
            maxWindow = max(maxWindow, r - l + 1)
        return len(s) - maxWindow

