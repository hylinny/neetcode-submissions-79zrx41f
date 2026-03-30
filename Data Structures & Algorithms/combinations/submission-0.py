class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # all possible length k combinations of distinct numbers within [1, n]
        # generate list of numbers from 1 to n
        # iterate through all of them and add to visited and decrement k
        # if k == 0, append array.copy() to output
        output = []
        array = [] # builds our combinations
        def generate(start, k):
            if k == 0:
                output.append(array.copy())
                return
            for i in range(start, n+1):
                array.append(i)
                generate(i+1, k-1)
                array.pop()
        generate(1, k)
        return output