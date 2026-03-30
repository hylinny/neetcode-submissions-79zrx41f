class Solution:

    def encode(self, strs: List[str]) -> str:
        outputlist = []
        for s in strs:
            length = len(s)
            outputlist.append(str(length) + '#')
            outputlist.append(s)
        return ''.join(outputlist)

    def decode(self, s: str) -> List[str]:
        outputlist = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            outputlist.append(s[i:j])
            i = j
        return outputlist

