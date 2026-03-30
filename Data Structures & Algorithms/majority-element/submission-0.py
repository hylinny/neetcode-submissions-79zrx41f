class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        freq = result = 0
        for key, value in hashmap.items():
            if value > freq:
                freq = value
                result = key
        return result
        