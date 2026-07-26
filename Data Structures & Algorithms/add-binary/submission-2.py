class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        if len(a) < len(b):
            a, b = b, a
        # a is the longer string
        output = []
        for i in range(-1, -len(a)-1, -1):
            if -i <= len(b) and b[i] == '1':
                carry += 1
            if a[i] == '1':
                carry += 1
            if carry == 0:
                output.append('0')
            elif carry == 1:
                carry = 0
                output.append('1')
            elif carry == 2:
                carry = 1
                output.append('0')
            elif carry == 3:
                carry = 1
                output.append('1')
        if carry == 1:
            output.append('1')
        return ''.join(reversed(output))

