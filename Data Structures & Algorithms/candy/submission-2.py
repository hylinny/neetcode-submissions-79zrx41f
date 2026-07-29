class Solution:
    def candy(self, ratings: List[int]) -> int:
        # [1, 2, 8, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 4, 3, 2, 1]
        # [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 1, 1, 1, 1]
        # [1, 1, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 4, 3, 2, 1]
        # [1, 2, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 4, 3, 2, 1]
        left = [1]
        right = [1]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left.append(left[-1] + 1)
            else:
                left.append(1)
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right.append(right[-1] + 1)
            else:
                right.append(1)
        right.reverse()
        candies = 0
        for i in range(len(left)):
            candies += max(left[i], right[i])
        return candies
