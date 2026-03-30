class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        # compute the sum so far
        fuel = 0
        index = 0
        for i in range(len(gas)):
            fuel += gas[i]
            fuel -= cost[i]
            if fuel < 0:
                fuel = 0
                index = i+1
        return index