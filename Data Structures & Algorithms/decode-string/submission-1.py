class Solution:
    def decodeString(self, s: str) -> str:
        # if we find a number, we recurse and
        # append to output "number" amount of times
        # if we encounter a closing parentheses,
        # we return the string we built so far
        index = 0 # global tracker
        def f():
            nonlocal index
            string = []
            while index < len(s):
                if s[index].isdigit():
                    left = index
                    while index < len(s)-1 and s[index+1].isdigit():
                        index += 1
                    number = s[left:index+1]
                    index += 2
                    str = f()
                    for i in range(int(number)):
                        string.extend(str)
                elif s[index].isalpha():
                    string.append(s[index])
                    index += 1
                elif s[index] == ']':
                    index += 1
                    break
            return string

        return ''.join(f())