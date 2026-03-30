class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for c in s:
            if c in parentheses:
                stack.append(c)
            else: # c is closing parentheses
                if not stack or parentheses[stack.pop()] != c:
                    return False
        return len(stack) == 0