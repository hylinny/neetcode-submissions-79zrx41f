class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 1 pass hashmap solution
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                if abs(hashmap[nums[i]] - i) <= k:
                    return True
            # otherwise, add nums[i] to hashmap and continue iterating
            hashmap[nums[i]] = i
        return False
        