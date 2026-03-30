class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # greedily take weights
        # binary search for value of max weight
        def solve(capacity):
            d = 1 # tracks days needed
            total = 0
            for weight in weights:
                if total + weight > capacity:
                    d += 1
                    total = weight
                else:
                    total += weight
            return d <= days
        l, r = max(weights), sum(weights)
        output = 0
        while l <= r:
            m = (r - l) // 2 + l
            if solve(m):
                output = m
                r = m - 1
            else:
                l = m + 1
        return output