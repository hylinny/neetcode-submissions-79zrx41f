class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # i and j tracks positions in s and p
        # alphabets: if s[i] == s[j], continue. else, rturn false
        # if either is ., proceed
        # if either is *, do a for loop and try proceeding either ways
        dp = {}
        def solve(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i < 0 and j < 0:
                return True
            if i < 0 and p[:j+1].count('*') * 2 != len(p[:j+1]) or j < 0 and s[:i+1].count('*') * 2 != len(s[:i+1]):
                return False
            dp[(i, j)] = False
            if s[i] == '*':
                print('s has *')
                for k in range(j, -2, -1):
                    if solve(i-2, k):
                        dp[(i, j)] = True
                        break
                    if s[i-1] != '.' and p[k] != '.' and s[i-1] != p[k]:
                        break
            elif p[j] == '*':
                print("p has *")
                for k in range(i, -2, -1):
                    # continue trying to take as long as chars match
                    if solve(k, j-2): # skip
                        dp[(i, j)] = True
                        break
                    if s[k] != '.' and p[j-1] != '.' and s[k] != p[j-1]:
                        # if not broken, it means we are taking s[k]
                        break
            elif s[i] == '.' or p[j] == '.':
                print("either has .")
                # s = '.', p = '.n*'
                dp[(i, j)] = solve(i-1, j-1)
            else: # both characters
                print('both characters')
                if s[i] == p[j]:
                    dp[(i, j)] = solve(i-1, j-1)
            return dp[(i, j)]
        return solve(len(s)-1, len(p)-1)
        # s = 'cdddc', p = cd*dddc
        # s = 'cdddc', p = cd*c
        # s = 'c...c', p = cd*c

