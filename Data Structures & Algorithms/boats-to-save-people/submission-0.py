class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sum of two people's weight must be <= limit
        # since each boat can only carry two people,
        # we can guarantee that matching largest and smallest 
        # elements is the optimal solution
        people.sort()
        l, r = 0, len(people)-1
        boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            else:
                boats += 1
                r -= 1
        return boats