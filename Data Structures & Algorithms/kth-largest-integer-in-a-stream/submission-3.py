class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minheap of size k
        self.heap = nums
        heapq.heapify(self.heap)
        self.capacity = len(self.heap)
        self.k = k
        while self.capacity > self.k:
            heapq.heappop(self.heap)
            self.capacity -= 1

    def add(self, val: int) -> int:
        if self.capacity < self.k:
            heapq.heappush(self.heap, val)
            self.capacity += 1
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]

        
