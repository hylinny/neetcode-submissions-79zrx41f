class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2
        l, r = 0, len(nums1)-1
        while True:
            m = (r - l) // 2 + l # nums1 index
            n = half - m - 2 # nums2 index
            left1 = nums1[m] if m >= 0 else float('-inf')
            right1 = nums1[m+1] if m+1 < len(nums1) else float('inf')
            left2 = nums2[n] if n >= 0 else float('-inf')
            right2 = nums2[n+1] if n+1 < len(nums2) else float('inf')

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return min(right1, right2)
            elif left1 > right2:
                r = m - 1
            else:
                l = m + 1


        # if r < 0, everything in nums2
        # if l == len(nums1), everything in nums1
