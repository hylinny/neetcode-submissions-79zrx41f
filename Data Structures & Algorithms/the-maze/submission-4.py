class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # need to keep track of direction. Ball must move forward until hitting a wall
        # our visited set must also keep track of direction! we can visit the same
        # cells but from different directions
        # we return true if next block is a wall, else return false
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        def dfs(i, j):
            if (i, j) in visited:
                return False
            if [i, j] == destination:
                return True
            visited.add((i, j))
            for dr, dc in directions:
                newi = i
                newj = j
                while 0 <= newi + dr < len(maze) and 0 <= newj + dc < len(maze[0]) and maze[newi + dr][newj + dc] == 0:
                    newi += dr
                    newj += dc
                if dfs(newi, newj):
                    return True
            return False

        return dfs(start[0], start[1])