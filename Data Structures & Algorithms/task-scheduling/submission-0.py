class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        bucket = [0] * 26
        for task in tasks:
            bucket[ord(task) - ord('A')] += 1
        highest = max(bucket) # task with highest frequency, greedily take this
        freq = bucket.count(highest) # how many tasks have this frequency
        bottleneck = (highest - 1) * (n + 1) + freq
        return max(bottleneck, len(tasks))
