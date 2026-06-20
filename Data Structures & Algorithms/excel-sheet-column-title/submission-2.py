class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        lst = []
        while columnNumber > 0:
            columnNumber -= 1
            lst.append(chr(ord('A') + (columnNumber % 26)))
            columnNumber //= 26
        return ''.join(reversed(lst))