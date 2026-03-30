class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = {'b': 0, 'a': 1, 'l': 2, 'o': 3, 'n': 4}
        output = [0] * 5 # [b, a, l, o, n]
        for c in text:
            if c in hashmap:
                output[hashmap[c]] += 1
        output[2] //= 2
        output[3] //= 2
        return min(output)

