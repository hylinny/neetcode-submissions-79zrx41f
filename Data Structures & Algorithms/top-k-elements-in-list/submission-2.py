class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        bucket = [[] for _ in range(len(nums)+1)]
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        for key, value in hashmap.items():
            bucket[value].append(key)
        output = []
        for i in range(len(bucket)-1, -1, -1):
            for j in range(len(bucket[i])):
                output.append(bucket[i][j])
                k -= 1
                if k == 0:
                    return output