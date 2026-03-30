class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointers
        # if left == right, move both inwards
        # else, check if left = right + 1 or left + 1 = right, and 
        # flip used to 0
        def check(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left, right = 0, len(s) - 1
        deleted = False
        while left < right:
            if s[left] != s[right]:
                return check(left+1, right) or check(left, right-1)
            left += 1
            right -= 1
        return True

        