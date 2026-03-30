class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        output = []
        # a appears twice, b is missing
        hashset = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in hashset:
                    output.append(grid[i][j])
                hashset.add(grid[i][j])
        for i in range(1, len(grid) ** 2 + 1):
            if i not in hashset:
                output.append(i)
                return output