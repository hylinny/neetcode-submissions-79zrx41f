class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute force: check starting from every index
        # accumulate gas so far
        # compare accumulated gas at index i and cost at index i 
        # if cost < gas, return false
        # if we successfully reach the end, return true
        # to loop around, take modulus
        n = len(gas)
        def solve(i):
            gasSoFar = 0
            for j in range(n):
                index = (i + j) % n # loop around logic
                gasSoFar += gas[index]
                gasSoFar -= cost[index]
                if gasSoFar < 0:
                    return -1
            return i

        for i in range(n):
            solution = solve(i)
            if solution != -1:
                return solution
        return -1

        