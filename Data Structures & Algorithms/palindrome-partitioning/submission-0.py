class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # iterate through s, and compare left and right boundaries
        # if is palindrome (use dp here), append to path and continue
        # if boundary exceeds, return
        dp = {}
        output = []
        def palindrome(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i > j:
                return True
            if s[i] != s[j]:
                dp[(i, j)] = False
                return False
            dp[(i, j)] = palindrome(i+1, j-1)
            return dp[(i, j)]
        def solve(path, start):
            if start >= len(s):
                output.append(path.copy())
                return
            for i in range(start, len(s)):
                if palindrome(start, i):
                    path.append(s[start:i+1])
                    solve(path, i+1)
                    path.pop()
        solve([], 0)
        return output
            
