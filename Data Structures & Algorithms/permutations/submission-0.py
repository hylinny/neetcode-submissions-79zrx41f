class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def f(array, builder):
            if len(array) == 0:
                output.append(builder)
                return
            for i in range(len(array)):
                b = builder[:]
                f(array[:i] + array[i+1:], b + [array[i]])
        
        f(nums, [])
        return output
