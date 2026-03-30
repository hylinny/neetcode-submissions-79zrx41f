class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # boundaries
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        output = [matrix[0][0]]
        x, y = 0, 0
        while left <= right and top <= bottom:
            while y < right:
                y += 1
                output.append(matrix[x][y])
            top += 1
            if top > bottom:
                break
            while x < bottom:
                x += 1
                output.append(matrix[x][y])
            right -= 1
            if left > right:
                break
            while y > left:
                y -= 1
                output.append(matrix[x][y])
            bottom -= 1
            if top > bottom:
                break
            while x > top:
                x -= 1
                output.append(matrix[x][y])
            left += 1
            if left > right:
                break
        return output


            
        