class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxLength = 0
        lengthSoFar = 0
        sign = -1 # -1 = invalid/equal, 1 = asc, 0 = desc
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                lengthSoFar = lengthSoFar + 1 if sign == 0 else 1
                sign = 1
            elif arr[i] < arr[i-1]:
                lengthSoFar = lengthSoFar + 1 if sign == 1 else 1
                sign = 0
            else:
                sign = -1
                lengthSoFar = 0
            maxLength = max(maxLength, lengthSoFar)
        return maxLength + 1