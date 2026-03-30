class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # we can choose to take current number, or skip it
        # if we choose to skip, we must skip all duplicates of this number
        candidates.sort()
        output = []
        array = []
        def solve(i, cum):
            if cum == target:
                output.append(array.copy())
                return
            if cum > target or i == len(candidates):
                return
            # choose to take
            array.append(candidates[i])
            solve(i+1, cum + candidates[i])
            array.pop()
            # choose to skip 
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            solve(i+1, cum)
        solve(0, 0)
        return output