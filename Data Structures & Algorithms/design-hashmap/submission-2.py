from bisect import insort_left, bisect_left

class MyHashMap:

    def __init__(self):
        # maintain sorted
        self.hashmap = []
        

    def put(self, key: int, value: int) -> None:
        i = bisect_left(self.hashmap, [key, -float('inf')])
        if i < len(self.hashmap) and self.hashmap[i][0] == key:
            self.hashmap[i][1] = value
        else:
            insort_left(self.hashmap, [key, value])

    def get(self, key: int) -> int:
        i = bisect_left(self.hashmap, [key, -float('inf')])
        if i < len(self.hashmap) and self.hashmap[i][0] == key:
            return self.hashmap[i][1]
        return -1
        

    def remove(self, key: int) -> None:
        i = bisect_left(self.hashmap, [key, -float('inf')])
        if i < len(self.hashmap) and self.hashmap[i][0] == key:
            del self.hashmap[i]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)