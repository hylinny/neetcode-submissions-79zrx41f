class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for num in nums:
            newDP = set()
            for i in dp:
                newDP.add(num+i)
            dp.update(newDP)
        return target in dp

        