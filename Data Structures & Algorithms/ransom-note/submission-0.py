class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineMap = defaultdict(int)
        for c in magazine:
            magazineMap[c] += 1
        for c in ransomNote:
            if magazineMap[c] == 0:
                return False
            magazineMap[c] -= 1
        return True