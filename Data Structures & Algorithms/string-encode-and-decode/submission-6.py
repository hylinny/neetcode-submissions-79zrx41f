class Solution:

    def encode(self, strs: List[str]) -> str:
        # add length of string + # to the start of each string
        array = []
        for s in strs:
            array.extend([str(len(s)), '#', s])
        return ''.join(array)

    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j+1
            word = s[i:i+length]
            output.append(word)
            i = i+length
        return output

