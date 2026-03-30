class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        encountered = [False, False, False]
        for triplet in triplets:
            if target[0] < triplet[0] or target[1] < triplet[1] or target[2] < triplet[2]:
                # we cannot use this triplet
                continue
            if target[0] == triplet[0]:
                encountered[0] = True
            if target[1] == triplet[1]:
                encountered[1] = True
            if target[2] == triplet[2]:
                encountered[2] = True
        return all(encountered)