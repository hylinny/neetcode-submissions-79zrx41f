class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def solve(paren, open, close):
            if close > open:
                return
            if open == n and close == n:
                output.append(paren)
            if open > n or close > n:
                return
            # try to append open or close
            solve(paren + '(', open + 1, close)
            solve(paren + ')', open, close + 1)
        solve('(', 1, 0)
        return output