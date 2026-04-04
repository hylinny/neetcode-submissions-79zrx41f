class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if abs(a - b) > 0:
                heapq.heappush(stones, -abs(a-b))
        return -stones[0] if stones else 0