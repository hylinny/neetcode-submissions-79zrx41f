class Solution:
    def maximumSwap(self, num: int) -> int:
        bestSwap = [-1, -1]
        maxNumber = -1
        maxIndex = -1
        nums = [int(i) for i in str(num)]
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > maxNumber:
                maxNumber = nums[i]
                maxIndex = i
            elif nums[i] < maxNumber:
                bestSwap = [i, maxIndex]
        if bestSwap[0] != -1:
            nums[bestSwap[0]], nums[bestSwap[1]] = nums[bestSwap[1]], nums[bestSwap[0]]
        return int(''.join(map(str, nums)))

