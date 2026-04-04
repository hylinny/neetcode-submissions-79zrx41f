class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calculate absolute distance to origin
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            d = math.sqrt(x * x + y * y)
            points[i].append(d)
        # quickselect to find kth element
        left, right = 0, len(points)-1
        while left <= right:
            pivot = points[left][2]
            l, r = left + 1, right
            while l <= r:
                if points[l][2] <= pivot:
                    l += 1
                else:
                    points[l], points[r] = points[r], points[l]
                    r -= 1
            # swap r with pivot
            points[left], points[r] = points[r], points[left]
            if r == k-1:
                return [[x, y] for x, y, z in points[:k]]
            elif r < k-1:
                left = r+1
            else:
                right = r-1
