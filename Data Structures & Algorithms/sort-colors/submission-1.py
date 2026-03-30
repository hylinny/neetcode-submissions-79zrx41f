class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        index = 0
        for i in range(hashmap[0]):
            nums[index] = 0
            index += 1
        for i in range(hashmap[1]):
            nums[index] = 1
            index += 1
        for i in range(hashmap[2]):
            nums[index] = 2
            index += 1
        