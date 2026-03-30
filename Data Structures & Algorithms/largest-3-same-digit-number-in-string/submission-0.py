class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxString = -1
        for i in range(len(num)-2):
            if len(set(num[i:i+3])) != 1:
                continue
            maxString = max(maxString, int(num[i:i+3]))

        if maxString == -1:
            return ""
        return str(maxString) if maxString != 0 else "000"