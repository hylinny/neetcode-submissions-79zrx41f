class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute force: check starting from every index
        # accumulate gas so far
        # compare accumulated gas at index i and cost at index i 
        # if cost < gas, return false
        # if we successfully reach the end, return true
        # to loop around, take modulus
        if sum(cost) > sum(gas):
            return -1
        n = len(gas)
        gasSoFar = 0
        solution = 0
        for i in range(n):
            gasSoFar += gas[i]
            gasSoFar -= cost[i]
            if gasSoFar < 0:
                gasSoFar = 0
                solution = i+1
        return solution


        