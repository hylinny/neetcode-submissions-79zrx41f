from math import prod

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # split array by zeroes
        # count number of negatives:
        # if negatives are even just multiple all regions together
        # and grab the max region
        # else: find the rightmost/leftmost negative number, multiply
        # the rest together, and grab the max

        # step 1: count number of zeroes
        arrays = [] # 0-separated array of arrays
        current = []
        for num in nums:
            if num == 0:
                if current:
                    arrays.append(current)
                current = []
            else:
                current.append(num)
        if current:
            arrays.append(current)

        maximum = max(nums)

        for array in arrays:
            negatives = sum(1 for i in array if i < 0)
            if negatives % 2 == 0:
                # even, just multiply all
                product = prod(array)
                maximum = max(maximum, product)
            else:
                # odd
                firstnegative = lastnegative = -1
                for i in range(len(array)):
                    if array[i] < 0:
                        firstnegative = i
                        break
                for i in range(len(array)-1, -1, -1):
                    if array[i] < 0:
                        lastnegative = i
                        break
                maxSoFar = float('-inf')
                if lastnegative > 0:
                    leftproduct = 1
                    for i in range(lastnegative):
                        leftproduct *= array[i]
                    maxSoFar = max(maxSoFar, leftproduct)
                if firstnegative + 1 < len(array):
                    rightproduct = 1
                    for i in range(len(array)-1, firstnegative, -1):
                        rightproduct *= array[i]
                    maxSoFar = max(maxSoFar, rightproduct)
                maximum = max(maxSoFar, maximum)

        return maximum








            