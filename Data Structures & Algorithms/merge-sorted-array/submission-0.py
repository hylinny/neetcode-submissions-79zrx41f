class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 3 pointers
        # fill in from the back
        l = m-1
        r = n-1
        for i in range(len(nums1)-1, -1, -1):
            if r < 0 or l >= 0 and nums1[l] > nums2[r]:
                nums1[i] = nums1[l]
                l -= 1
            else:
                nums1[i] = nums2[r]
                r -= 1
        