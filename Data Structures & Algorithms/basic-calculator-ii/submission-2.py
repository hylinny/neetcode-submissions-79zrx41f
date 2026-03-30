class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '*':
                x = int(stack.pop())
                i += 1
                integer = []
                while i < len(s) and s[i].isdigit():
                    integer.append(s[i])
                    i += 1
                y = int(''.join(integer))
                stack.append(x * y)
            elif s[i] == '/':
                x = int(stack.pop())
                i += 1
                integer = []
                while i < len(s) and s[i].isdigit():
                    integer.append(s[i])
                    i += 1
                y = int(''.join(integer))
                stack.append(int(x / y))
            elif s[i] in ['+', '-']:
                stack.append(s[i])
                i += 1
            else: # number
                integer = []
                while i < len(s) and s[i].isdigit():
                    integer.append(s[i])
                    i += 1
                stack.append(int(''.join(integer)))
        print(stack)
        stack2 = []
        i = 0
        while i < len(stack):
            if stack[i] == '+':
                x = stack2.pop()
                y = int(stack[i+1])
                stack2.append(x + y)
                i += 2
            elif stack[i] == '-':
                x = stack2.pop()
                y = int(stack[i+1])
                stack2.append(x - y)
                i += 2
            else:
                stack2.append(int(stack[i]))
                i += 1
        return stack2[0]
