class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        output = []
        n = len(nums)
        for key, value in hashmap.items():
            if value > n // 3:
                output.append(key)
        return output