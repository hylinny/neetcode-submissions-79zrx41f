class CountSquares:

    def __init__(self):
        self.hashmap = defaultdict(int) # stores coordinates to frequencies

    def add(self, point: List[int]) -> None:
        self.hashmap[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        newx, newy = point[0], point[1]
        cnt = 0
        for (x, y), freq in self.hashmap.items():
            if newx != x and newy != y and abs(x - newx) == abs(y - newy):
                # potential square
                if (newx, y) in self.hashmap and (x, newy) in self.hashmap:
                    cnt += self.hashmap[(x, y)] * self.hashmap[(newx, y)] * self.hashmap[(x, newy)]
            
        return cnt
        
