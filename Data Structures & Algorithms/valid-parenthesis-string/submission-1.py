class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == '*':
                stars.append(i)
            else:
                if not stack and not stars:
                    return False
                elif stack:
                    stack.pop()
                else:
                    stars.pop()
        while stack and stars:
            if stack.pop() > stars.pop():
                return False
        return len(stack) == 0