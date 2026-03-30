import heapq

class MedianFinder:
    # maintain two heaps, minheap and maxheap
    # minheap contains smaller half,
    # maxheap contains larger half
    # always add to maxheap if even

    def __init__(self):
        self.smallheap = [] # largest of lower half on top (-ve)
        self.largeheap = [] # smallest of upper half on top
        self.count = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.largeheap, num)
        heapq.heappush(self.smallheap, -heapq.heappop(self.largeheap))

        if len(self.smallheap) > len(self.largeheap):
            # maintains largeheap always >= smallheap by 0-1
            heapq.heappush(self.largeheap, -heapq.heappop(self.smallheap))

    def findMedian(self) -> float:
        if len(self.largeheap) > len(self.smallheap):
            return self.largeheap[0]
        return (self.largeheap[0] - self.smallheap[0]) / 2
        
        
        