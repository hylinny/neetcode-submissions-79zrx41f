class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # we can have at most 2 consecutive strings of same letter
        # 'bb_bb_bb_aa'
        # a=5, b=6
        # 'bbaabb__bb
        # a=2, b=6
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, 'a'))
        if b > 0:
            heapq.heappush(pq, (-b, 'b'))
        if c > 0:
            heapq.heappush(pq, (-c, 'c'))
        output = []
        while pq:
            mostfreq, char = heapq.heappop(pq)
            mostfreq = -mostfreq
            # print(f'start: mostfreq = {mostfreq}, char = {char}')
            if len(output) >= 2 and output[-1] == output[-2] == char:
                # print('if')
                # violated max 2 consec, must take new one
                if not pq:
                    return ''.join(output)
                nextfreq, nextchar = heapq.heappop(pq)
                nextfreq = -nextfreq
                output.append(nextchar)
                if nextfreq-1 > 0:
                    heapq.heappush(pq, (-(nextfreq-1), nextchar))
                heapq.heappush(pq, (-mostfreq, char))
            else:
                # print('else')
                output.append(char)
                if mostfreq-1 > 0:
                    heapq.heappush(pq, (-(mostfreq-1), char))
        return ''.join(output)