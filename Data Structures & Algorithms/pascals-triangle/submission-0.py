class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        output = [[1]]
        for i in range(numRows-1):
            result = [1]
            for j in range(1, len(output[-1])):
                result.append(output[-1][j-1] + output[-1][j])
            result.append(1)
            output.append(result)
        return output