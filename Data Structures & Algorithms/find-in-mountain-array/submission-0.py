class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # increasing then decreasing array
        # target can either be left or right side or none. if both, return left side
        # first binary search finds peak (peak finding, elements strict)
        # second one searches both sides
        n = mountainArr.length()
        l, r = 0, n - 1
        while l < r:
            m = (r - l) // 2 + l
            if mountainArr.get(m) < mountainArr.get(m+1):
                l = m + 1
            else:
                r = m
        # l == r, points to peak 
        # search left side first
        peak = l
        l, r = 0, peak
        while l <= r:
            m = (r - l) // 2 + l
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val < target:
                l = m + 1
            else:
                r = m - 1
        l, r = peak + 1, n-1
        while l <= r:
            m = (r - l) // 2 + l
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val < target:
                r = m - 1
            else:
                l = m + 1
        return -1