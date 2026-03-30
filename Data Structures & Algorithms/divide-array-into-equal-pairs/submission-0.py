class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        for key, value in hashmap.items():
            if value % 2 != 0:
                return False
        return True
