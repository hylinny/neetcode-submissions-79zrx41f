class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # at the current step, we check if we can
        # add the next s3 character to either i+1, or j+1
        # if not, just return false
        # initial check: len(s1) + len(s2) = len(s3)
        memo = {}
        if len(s1) + len(s2) != len(s3):
            return False
        def solution(i, j):
            if i >= len(s1):
                return s2[j:len(s2)] == s3[i+j:len(s3)]
            if j >= len(s2):
                return s1[i:len(s1)] == s3[i+j:len(s3)]
            if (i, j) in memo:
                return memo[(i, j)]
            # recursion step
            isValid = False
            if s1[i] == s3[i+j]:
                isValid = isValid or solution(i+1, j)
            if not isValid and s2[j] == s3[i+j]:
                isValid = isValid or solution(i, j+1)
            memo[(i, j)] = isValid
            return memo[(i, j)]
        return solution(0, 0)



