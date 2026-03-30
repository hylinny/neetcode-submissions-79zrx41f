class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestSoFar = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = greatestSoFar
            if temp > greatestSoFar:
                greatestSoFar = temp
        return arr