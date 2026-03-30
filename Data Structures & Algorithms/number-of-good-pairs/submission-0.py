class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        for i in range(len(nums)):
            hashmap[nums[i]].append(i)

        output = 0
        for i in range(len(nums)):
            if nums[i] in hashmap:
                array = hashmap[nums[i]]
                for index in array:
                    if index < i:
                        output += 1
        return output