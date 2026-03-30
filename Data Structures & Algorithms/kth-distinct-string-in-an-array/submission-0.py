class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = defaultdict(int)
        for num in arr:
            hashmap[num] += 1
        for key, value in hashmap.items():
            if value > 1:
                continue
            k -= 1
            if k == 0:
                return key
        return ""