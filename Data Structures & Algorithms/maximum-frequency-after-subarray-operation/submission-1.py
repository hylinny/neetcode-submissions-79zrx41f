class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # largest frequency of k and another number
        kcount = nums.count(k)
        maxFreq = 0
        for i in range(1, 51):
            if i == k:
                continue
            count = 0
            for num in nums:
                if num == i:
                    count += 1
                if num == k:
                    count -= 1
                if count < 0:
                    count = 0
                maxFreq = max(maxFreq, count + kcount)
        return maxFreq
        