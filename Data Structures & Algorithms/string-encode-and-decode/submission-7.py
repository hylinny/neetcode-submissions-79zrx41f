class Solution:

    def encode(self, strs: List[str]) -> str:
        # hash + number + hash to denote length of string
        encoding = []
        for string in strs:
            encoding.append(str(len(string)))
            encoding.append('#')
            encoding.append(string)
        return ''.join(encoding)

    def decode(self, s: str) -> List[str]:
        output = []
        left = right = 0
        while right < len(s):
            while s[right] != '#':
                right += 1
            length = int(s[left:right])
            right += 1 # move past the #
            string = s[right:right+length]
            output.append(string)
            right = right + length
            left = right
        return output
