class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        if len(str1) > len(str2):
            a = len(str1)
            b = len(str2)
        else:
            a = len(str2)
            b = len(str1)
        while a % b != 0:
            # a = qb + r, a > b
            # gcd(a, b) = gcd(b, r)
            a, b = b, a % b
        return str1[:b]
