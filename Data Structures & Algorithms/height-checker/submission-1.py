class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # build expected array
        count = [0] * 101
        for h in heights:
            count[h] += 1
        expected = []
        for i in range(len(count)):
            while count[i] > 0:
                expected.append(i)
                count[i] -= 1
        output = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                output += 1
        return output