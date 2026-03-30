class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        output = ""
        for i in range(len(min(strs, key=len))):
            c = strs[0][i]
            for str in strs:
                if str[i] != c:
                    return output
            output += c
        return output