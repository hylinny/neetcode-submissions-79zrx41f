class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # maintain sliding window of size k
        # when moving window, if right is W -> +1 operation, if left is W -> -1 operation
        minOperations = 0
        for i in range(k):
            if blocks[i] == 'W':
                minOperations += 1
        l = 0
        delta = minOperations
        for r in range(k-1, len(blocks)-1):
            # try sliding window to the right
            if blocks[r+1] == 'W':
                delta += 1
            if blocks[l] == 'W':
                delta -= 1
            l += 1
            minOperations = min(minOperations, delta)
        return minOperations

        