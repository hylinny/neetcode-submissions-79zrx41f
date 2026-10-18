class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # largest frequency of k and another number
        freqMap = defaultdict(int)
        profit = 0
        for num in nums:
            freqMap[num] = max(freqMap[num], freqMap[k]) + 1
            profit = max(profit, freqMap[num] - freqMap[k])
        return profit + freqMap[k]
        