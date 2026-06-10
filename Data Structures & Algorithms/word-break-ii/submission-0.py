class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        output = []
        dictionary = set(wordDict)
        def solve(i, sentence):
            if i == len(s):
                output.append(''.join(sentence[:-1]))
                return
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word in dictionary:
                    sentence.append(word)
                    sentence.append(' ')
                    solve(j+1, sentence)
                    sentence.pop()
                    sentence.pop()
        solve(0, [])
        return output

