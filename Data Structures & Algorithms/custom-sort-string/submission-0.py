class Solution:
    def customSortString(self, order: str, s: str) -> str:
        output = []
        hashmap = defaultdict(int)
        for c in s:
            hashmap[c] += 1
        for c in order:
            if c in hashmap:
                while hashmap[c] > 0:
                    output.append(c)
                    hashmap[c] -= 1
        for key in hashmap:
            while hashmap[key] > 0:
                output.append(key)
                hashmap[key] -= 1
        return ''.join(output)