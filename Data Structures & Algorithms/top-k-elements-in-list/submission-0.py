class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        minheap = []
        for num, frequency in hashmap.items():
            heapq.heappush(minheap, (-frequency, num))
        output = []
        for i in range(k):
            output.append(heapq.heappop(minheap)[1])
        return output
