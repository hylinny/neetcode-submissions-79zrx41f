class ListNode:
    def __init__(self, key=0, value=0, freq=0, prev=None, next=None):
        self.key = key
        self.freq = freq
        self.prev = prev
        self.next = next
        self.value = value

class DoublyLinkedList:
    def __init__(self, freq):
        self.count = 0
        self.freq = freq
        self.head, self.tail = ListNode(), ListNode() # dummy head / tail    
        self.head.next, self.tail.prev = self.tail, self.head

class LFUCache:

    def __init__(self, capacity: int):
        self.keymap = {} # maps keys to nodes for instant access
        self.freqmap = {} # maps access frequencies to DLLs
        self.capacity = capacity
        self.elements = 0
        self.minfreq = -1 # minfreq integer
    
    def incrementFreq(self, node):
        # move node from freqmap[i] to freqmap[i+1]
        node.prev.next, node.next.prev = node.next, node.prev # detach from original DLL
        frequency = node.freq
        dll = self.freqmap[frequency]
        dll.count -= 1
        if dll.count == 0 and frequency == self.minfreq:
            self.minfreq += 1
        # now, we insert to new dll's head
        node.freq += 1
        if frequency + 1 not in self.freqmap:
            newdll = DoublyLinkedList(frequency + 1)
            self.freqmap[frequency+1] = newdll
        newdll = self.freqmap[frequency+1]
        temp = newdll.head.next
        newdll.head.next = node
        node.prev = newdll.head
        node.next = temp
        temp.prev = node
        newdll.count += 1
        
    def get(self, key: int) -> int:
        # if key exists, return it and increment use counter
        if key not in self.keymap:
            return -1
        node = self.keymap[key]
        self.incrementFreq(node)
        # print("get operation start")
        # print(f"node.key = {node.key}")
        # dll = self.freqmap[1]
        # curr = dll.head
        # print('freq map 1:')
        # while curr:
        #     print(curr.key)
        #     curr = curr.next
        # print('freq map 2:')
        # dll = self.freqmap[2]
        # curr = dll.head
        # while curr:
        #     print(curr.key)
        #     curr = curr.next
        # print(f"minfreq = {self.minfreq}")
        # print('get operation end')
        return node.value

    def put(self, key: int, value: int) -> None:
        # update value of key with usage frequency
        # if not present, insert if capacity not full
        # if capacity full, kick out least frequently used element
        if key in self.keymap:
            self.get(key)
            node = self.keymap[key]
            node.value = value
            return
        # else, we insert the key
        if self.elements == self.capacity:
            # kick out LFU key
            dll = self.freqmap[self.minfreq]
            lfunode = dll.tail.prev
            lfunode.prev.next, lfunode.next.prev = lfunode.next, lfunode.prev
            dll.count -= 1
            self.elements -= 1
            del self.keymap[lfunode.key]
        # insert new key into frequency count of 1
        node = ListNode(key, value, 1)
        if 1 not in self.freqmap:
            newdll = DoublyLinkedList(1)
            self.freqmap[1] = newdll
        newdll = self.freqmap[1]
        temp = newdll.head.next
        newdll.head.next = node
        node.prev = newdll.head
        node.next = temp
        temp.prev = node
        newdll.count += 1
        self.elements += 1
        self.minfreq = 1
        self.keymap[key] = node
        # debugging
        # dll = self.freqmap[1]
        # curr = dll.head
        # print('put operation start')
        # while curr:
        #     print(curr.key)
        #     curr = curr.next
        # print(f"minfreq = {self.minfreq}")
        # print('put operation end')
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)