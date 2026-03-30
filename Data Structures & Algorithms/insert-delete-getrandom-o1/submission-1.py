import random

class RandomizedSet:

    def __init__(self):
        # hashmap maps number to array index
        self.hashmap = {}
        self.array = []
        self.lastIndex = -1

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.array.append(val)
        self.lastIndex += 1
        self.hashmap[val] = self.lastIndex
        return True

    def remove(self, val: int) -> bool:
        # swap value in array with last element in array for O(1) removal
        if val not in self.hashmap:
            return False
        index = self.hashmap[val]
        lastValue = self.array[-1]
        self.array[index], self.array[-1] = self.array[-1], self.array[index]
        self.hashmap[lastValue] = index
        del self.hashmap[val]
        self.array.pop()
        self.lastIndex -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()