class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # greedily remove first senator to the right
        # two queues
        # add indices to the queue
        # compare indices, if one earlier than other, remove other fella
        # indices would never be the same
        r, d = deque(), deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
            rIndex = r.popleft()
            dIndex = d.popleft()
            if rIndex < dIndex:
                # radiant can ban dire
                r.append(rIndex + n)
            else:
                d.append(dIndex + n)
        return "Radiant" if r else "Dire"