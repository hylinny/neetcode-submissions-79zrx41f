class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # heaps, storing end time with room number
        # as end time gets popped, room frees up
        # next available start time gets popped and room occupies itself
        # hashmap to store number of times each room got used
        # n = 2, meetings = [[0, 5], [6, 10]]
        frequency = [0] * n
        endHeap = []
        meetingsHeap = [i for i in range(n)] # already a min heap
        meetings.sort()
        for meeting in meetings:
            while endHeap and meeting[0] >= endHeap[0][0]:
                endTime, roomNumber = heapq.heappop(endHeap)
                heapq.heappush(meetingsHeap, roomNumber)
            if meetingsHeap:
                meetingRoom = heapq.heappop(meetingsHeap)
                heapq.heappush(endHeap, (meeting[1], meetingRoom))
                frequency[meetingRoom] += 1
            else:
                endTime, roomNumber = heapq.heappop(endHeap)
                availableRoom = heapq.heappushpop(meetingsHeap, roomNumber)
                delay = 0
                if meeting[0] < endTime:
                    delay = endTime - meeting[0]
                heapq.heappush(endHeap, (meeting[1] + delay, availableRoom))
                frequency[availableRoom] += 1
        return frequency.index(max(frequency))
                
        