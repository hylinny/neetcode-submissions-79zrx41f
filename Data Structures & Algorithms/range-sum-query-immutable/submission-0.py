class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefixSum.append(self.prefixSum[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        l = 0 if left == 0 else self.prefixSum[left-1]
        return self.prefixSum[right] - l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)