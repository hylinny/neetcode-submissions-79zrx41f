class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # track ending indices
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = i
        output = []
        length = 0
        end = 0
        for i in range(len(s)):
            end = max(end, hashmap[s[i]])
            length += 1
            if i == end:
                output.append(length)
                length = 0
        return output