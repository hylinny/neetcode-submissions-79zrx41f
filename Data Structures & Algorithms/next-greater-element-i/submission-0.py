class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for num in nums1:
            i = 0
            while i < len(nums2) and nums2[i] != num:
                # find the element num in nums2
                i += 1
            # at this point, nums2[i] == num
            while i < len(nums2):
                if nums2[i] > num:
                    output.append(nums2[i])
                    break
                i += 1
            # next greater element not found
            if i == len(nums2):
                output.append(-1)

        return output
            