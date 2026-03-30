class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # no length difference constraints
        # no arbitrary matching constraints
        leftmap = rightmap = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(s)):
            left = pattern[i]
            right = s[i]
            if left in leftmap and leftmap[left] != right or right in rightmap and rightmap[right] != left:
                return False
            if left not in leftmap:
                leftmap[left] = right
            if right not in rightmap:
                rightmap[right] = left
        return True