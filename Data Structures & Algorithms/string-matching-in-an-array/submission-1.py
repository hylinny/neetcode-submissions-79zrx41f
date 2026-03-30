class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] != words[j] and words[i] in words[j]:
                    output.append(words[i])
                    break
        return output