class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search for the value of k
        # min is 1, max is max(piles)
        # call function to eat from piles
        def eat(k):
            hours = h
            for pile in piles:
                hours -= math.ceil(pile / k)
                if hours < 0:
                    return False
            return hours >= 0
        l, r = 1, max(piles)
        target = -1
        while l <= r:
            m = (r - l) // 2 + l
            if eat(m):
                target = m
                r = m - 1
            else:
                l = m + 1
        return target
                
                    