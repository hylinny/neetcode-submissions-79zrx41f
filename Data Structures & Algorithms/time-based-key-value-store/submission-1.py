class TimeMap:

    def __init__(self):
        # same key stores multiple values
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        array = self.hashmap[key]
        target = ""
        l, r = 0, len(array)-1
        while l <= r:
            m = (r - l) // 2 + l
            if array[m][1] <= timestamp:
                target = array[m][0]
                l = m + 1
            else:
                r = m - 1
        return target
