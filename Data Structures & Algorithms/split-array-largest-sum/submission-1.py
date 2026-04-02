class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # binary search solution
        l, r = max(nums), sum(nums)
        def greedy(maxSum):
            splits = 1
            curSum = 0
            for num in nums:
                if curSum + num > maxSum:
                    curSum = num
                    splits += 1
                else:
                    curSum += num
                if splits > k:
                    return False
            return True
        output = -1
        while l <= r:
            m = (r - l) // 2 + l
            if greedy(m):
                output = m
                r = m - 1
            else:
                l = m + 1
        return output
