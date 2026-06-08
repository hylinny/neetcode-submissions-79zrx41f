class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        output = []
        def solve(i, array):
            if i == len(digits):
                output.append(''.join(array))
                return
            letters = hashmap[digits[i]]
            for l in letters:
                array.append(l)
                solve(i+1, array)
                array.pop()
        solve(0, [])
        return output