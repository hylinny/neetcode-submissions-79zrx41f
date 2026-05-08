class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {c: i for i, c in enumerate(order)}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if dictionary[word1[j]] > dictionary[word2[j]]:
                        return False
                    break
        return True