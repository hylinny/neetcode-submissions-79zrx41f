import random

class RandomizedSet:

    def __init__(self):
        self.hashmap = {} # maps values to their indices in array
        self.array = []

    def insert(self, val: int) -> bool:
        # insert if not present, return if present
        if val not in self.hashmap:
            self.hashmap[val] = len(self.array)
            self.array.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        # remove if present, return true
        if val in self.hashmap:
            index = self.hashmap[val] # grabs index of value to be deleted
            swap = self.array[-1] # grab last element in array
            self.hashmap[swap] = index # grab index of old last element
            self.array[index] = swap # put last element into deleted value's position
            self.array.pop()
            del self.hashmap[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        # return any element with equal probability
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()