class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = defaultdict(int)
        for c in s:
            hashmap[c] += 1
        maxOdd = float('-inf')
        minEven = float('inf')
        for character, count in hashmap.items():
            if count % 2 == 0: # even
                minEven = min(minEven, count)
            else:
                maxOdd = max(maxOdd, count)
        return maxOdd - minEven