class Solution:
    def decodeString(self, s: str) -> str:
        # recursive solution
        # called when we encounter opening [
        # if letter -> add to string
        # if number -> add to k * 10
        # if [, then retrieve string from 
        # recursive call and multiply by k
        i = 0
        def solve():
            nonlocal i
            string = ''
            k = 0
            while i < len(s):
                if s[i].isdigit():
                    k = k * 10 + int(s[i])
                    i += 1
                elif s[i] == '[':
                    i += 1
                    string += k * solve()
                    k = 0
                elif s[i] == ']':
                    i += 1
                    return string
                else:
                    string += s[i]
                    i += 1
            return string
        return solve()