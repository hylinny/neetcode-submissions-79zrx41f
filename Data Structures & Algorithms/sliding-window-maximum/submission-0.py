class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        heap = []
        l = 0
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        output.append(-heap[0][0]) # peek at max element
        # at this point, first window is already filled with values
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            l += 1
            while heap[0][1] < l:
                heapq.heappop(heap)
            output.append(-heap[0][0])
        return output
