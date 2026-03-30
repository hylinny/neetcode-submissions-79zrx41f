class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # so that we can skip over duplicates
        # each element can be chosen at most once
        output = []
        array = []
        def solve(i, cum):
            if cum == target:
                output.append(array.copy())
                return
            if i == len(candidates) or cum > target:
                return
            # choose to add current element, or skip
            # take current element
            array.append(candidates[i])
            solve(i+1, cum + candidates[i])
            array.pop()
            # if we choose to skip, we must skip all duplicates of it
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            solve(i+1, cum)
        solve(0, 0)
        return output
