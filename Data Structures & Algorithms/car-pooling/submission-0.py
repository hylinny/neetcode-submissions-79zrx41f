class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # can drop off and pick up immediately
        # interval line: maximum overlap <= capacity for validity
        # 2 heaps: start heap and end heap, each storing all info
        # don't care about whether start matches end
        startheap = []
        endheap = []
        for passengers, start, end in trips:
            heapq.heappush(startheap, (start, end, passengers))
            heapq.heappush(endheap, (end, start, passengers))
        load = 0
        while startheap: # if we clear startheap and all works, we can be sure its possible without clearing endheap           
            if startheap[0] < endheap[0]:
                start, end, passengers = heapq.heappop(startheap)
                load += passengers
                if load > capacity:
                    return False
            else:
                end, start, passengers = heapq.heappop(endheap)
                load -= passengers
        return True
