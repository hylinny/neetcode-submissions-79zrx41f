class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                # do computation, then append result back to stack
                first = stack.pop()
                second = stack.pop()
                stack.append(first + second)
            elif token == '*':
                first = stack.pop()
                second = stack.pop()
                stack.append(first * second)
            elif token == '-':
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif token == '/':
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second/first))
            else: # value is digit
                stack.append(int(token))
        return stack[-1]