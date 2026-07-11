class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # if k reached, return price
        flightMap = defaultdict(list)
        for frm, to, price in flights:
            flightMap[frm].append((to, price))
        dp = {}
        def solve(airport, steps):
            if (airport, steps) in dp:
                return dp[(airport, steps)]
            if airport == dst:
                return 0
            if steps > k:
                return float('inf')
            # currently, we are at airport
            minPrice = float('inf')
            for to, px in flightMap[airport]:
                minPrice = min(minPrice, px + solve(to, steps + 1))
            dp[(airport, steps)] = minPrice
            return minPrice
        price = solve(src, 0)
        return price if price != float('inf') else -1
            