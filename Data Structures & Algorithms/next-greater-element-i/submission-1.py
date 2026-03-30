class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1map = {value: i for i, value in enumerate(nums1)}
        output = [-1] * len(nums1)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                value = stack.pop()
                index = nums1map[value]
                output[index] = num
            if num in nums1map:
                stack.append(num)
        return output
            