class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = 0
        while curr < len(path):
            if path[curr] == '/':
                while curr < len(path) and path[curr] == '/':
                    curr += 1
                stack.append(path[curr-1])
            else: # series of dots or alphabets
                stringArray = []
                while curr < len(path) and path[curr] != '/':
                    stringArray.append(path[curr])
                    curr += 1
                string = ''.join(stringArray)
                if string == '.':
                    # current directory, don't do anything, just pop '/'
                    stack.pop()
                elif string == '..':
                    # go back one directory
                    stack.pop()
                    if stack:
                        stack.pop()
                        stack.pop()
                else: # valid directory / file name
                    stack.append(string)
                
        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()
        elif len(stack) == 0:
            stack.append('/')
        return ''.join(stack)

        