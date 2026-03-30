class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        buckets = [[] for _ in range(len(nums)+1)]
        # frequency of any element is at most len(nums)
        for key, freq in hashmap.items():
            buckets[freq].append(key)
        output = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                output.append(num)
                k -= 1
            if k == 0:
                return output
        # return output