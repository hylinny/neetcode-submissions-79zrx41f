class Solution:
    def isHappy(self, n: int) -> bool:
        numberSet = set()
        while True:
            digitSum = 0
            for x in str(n):
                digitSum += int(x) ** 2
            if digitSum == 1:
                return True
            if digitSum in numberSet:
                return False
            numberSet.add(digitSum)
            n = digitSum