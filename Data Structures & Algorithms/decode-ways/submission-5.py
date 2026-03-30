class Solution:
    def numDecodings(self, s: str) -> int:
        # A -> 1 ... Z -> 26
        # iterate through s
        # if we encounter a single number, calculate solve(i+1)
        # add that to calculating single number + next number
        # as long as next number exists and 1 <= number <= 26
        # return the sum
        def solve(i):
            if i == len(s):
                return 1
            ways = 0
            if s[i] != '0':
                ways += solve(i+1)
                if i < len(s)-1 and 1 <= int(s[i:i+2]) <= 26:
                    ways += solve(i+2)
            return ways
        output = solve(0)
        return output if output != float('inf') else 0