class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # skill = [2, 2, 8, 4, 6, 6, 6, 6]
        # skill = [3, 2, 5, 1, 3, 4]
        totalSum = sum(skill)
        n = len(skill)
        if totalSum % (n // 2) != 0:
            return -1
        hashmap = defaultdict(int)
        for x in skill:
            hashmap[x] += 1
        skillValue = totalSum // (n // 2)
        solution = 0
        for x in skill:
            if hashmap[skillValue - x] == 0:
                return -1
            hashmap[skillValue - x] -= 1
            solution += x * (skillValue - x)
        return solution // 2


# {
#     3 -> 0
#     2 -> 0
#     5 -> 0
#     1 -> 0
#     4 -> 0
# }
            