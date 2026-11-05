class Number:
    def __init__(self, num):
        self.num = str(num)

    def __lt__(self, other):
        num1, num2 = self.num, other.num
        # find the LCM of both numbers
        n = math.lcm(len(num1), len(num2))
        a = b = 0
        for i in range(n):
            if a == len(num1):
                a = 0
            if b == len(num2):
                b = 0
            if int(num1[a]) < int(num2[b]):
                return True
            elif int(num1[a]) > int(num2[b]):
                return False
            a += 1
            b += 1
        return True 

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        allZeroes = True
        for i in range(len(nums)):
            if nums[i] > 0:
                allZeroes = False
            nums[i] = Number(nums[i])
        if allZeroes:
            return '0'
        nums.sort(reverse=True)
        return ''.join(number.num for number in nums)