class Solution:
    def minEnd(self, n: int, x: int) -> int:
        binary = []
        curr = n-1
        while curr > 0:
            binary.append(curr % 2)
            curr //= 2
        output = 0
        curr = x
        i = j = 0
        while curr > 0:
            if curr % 2 == 0:
                if i >= len(binary):
                    return x | output
                output += (2 ** j) * binary[i]
                i += 1
            j += 1
            curr //= 2
        while i < len(binary):
            output += (2 ** j) * binary[i]
            i += 1
            j += 1
        return output | x
        


            

