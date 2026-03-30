class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search to find location of x,
        # then maintain two pointers going left and right
        # ^^ while l >= 0 and r < len(arr)
        def bs():
            l, r = 0, len(arr) - 1
            while l < r:
                m = (r - l) // 2 + l
                if arr[m] < x:
                    l = m + 1
                else:
                    r = m
            return l
        
        result = []
        index = bs()
        # index is slightly above or equal to x
        l, r = index-1, index
        while k > 0:
            while k > 0 and l >= 0 and r < len(arr):
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    result.append(arr[l])
                    l -= 1
                else:
                    result.append(arr[r])
                    r += 1
                k -= 1
            if k == 0:
                break
            if r == len(arr):
                result.append(arr[l])
                l -= 1
                k -= 1
            if l < 0:
                result.append(arr[r])
                r += 1
                k -= 1
        result.sort()
        return result
        