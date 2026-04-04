class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        largest = max(stones)
        bucket = [0] * (largest + 1)
        for stone in stones:
            bucket[stone] += 1
        while largest > 0:
            if bucket[largest] % 2 == 0:
                largest -= 1
                continue
            bucket[largest] = 0
            second = largest
            while second > 0 and bucket[second] == 0:
                second -= 1
            if second == 0:
                break
            # try smashing them together
            new = largest - second
            bucket[second] -= 1
            bucket[new] += 1
            largest = max(new, second)
        return largest