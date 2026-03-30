class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 3 choices in decision tree: insert, delete, replace
        # i, j to track word1, word2
        # base case: empty string matches
        # recurrence: if word1[i] == word2[j], we return 0 (do nothing)
        # else: try the 3 choices and grab return minimum 
        dp = {}
        def solution(i, j):
            if i >= len(word1):
                return len(word2)-j
            if j >= len(word2):
                return len(word1)-i
            if (i, j) in dp:
                return dp[(i, j)]
            # recurrence
            if word1[i] == word2[j]:
                return solution(i+1, j+1)
            else:
                dp[(i, j)] = min(
                    1 + solution(i+1, j), # delete character
                    1 + solution(i, j+1), # insert character
                    1 + solution(i+1, j+1) # replace character
                )
                return dp[(i, j)]
        return solution(0, 0)
        