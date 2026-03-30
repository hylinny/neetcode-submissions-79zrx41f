class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sortednums = sorted(nums)
        for i in range(len(sortednums)):
            if sortednums[i] > 0:
                break
            if i > 0 and sortednums[i] == sortednums[i-1]:
                continue
            left, right = i + 1, len(sortednums) - 1
            while left < right:
                threesum = sortednums[left] + sortednums[right] + sortednums[i]
                if threesum < 0:
                    left += 1
                elif threesum > 0:
                    right -= 1
                else: # threesum == 0
                    output.append([sortednums[left], sortednums[right], sortednums[i]])
                    left += 1
                    right -= 1
                    while left < right and sortednums[left] == sortednums[left-1]:
                        left += 1
        return output