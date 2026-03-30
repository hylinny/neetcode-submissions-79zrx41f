class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        hashmap = defaultdict(int)
        for c in s:
            hashmap[c] += 1
        for c in t:
            hashmap[c] -= 1
        for value in hashmap.values():
            if value != 0:
                return False
        return True            