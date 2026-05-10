class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # bfs search
        # at each iteration, try changing each number up and down
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        queue = deque()
        visited = set()
        queue.append('0000')
        visited.add('0000')
        turns = 0
        while queue:
            l = len(queue)
            for i in range(l):
                state = queue.popleft()
                if state == target:
                    return turns
                for j in range(len(state)):
                    down = str((int(state[j]) - 1) % 10)
                    up = str((int(state[j]) + 1) % 10)
                    newstate1 = state[:j] + down + state[j+1:]
                    newstate2 = state[:j] + up + state[j+1:]
                    if newstate1 not in deadends and newstate1 not in visited:
                        visited.add(newstate1)
                        queue.append(newstate1)
                    if newstate2 not in deadends and newstate2 not in visited:
                        visited.add(newstate2)
                        queue.append(newstate2)
            turns += 1
        return -1
                    
