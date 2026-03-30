class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {} # maps keys to node values
        self.head, self.tail = Node(0, 0), Node(0, 0) # dummy nodes 
        self.head.next, self.tail.prev = self.tail, self.head
        # head is LRU

    def remove(self, node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev
    
    def insert(self, node) -> None:
        # insert node to the end of the linked list
        prev = self.tail.prev
        nxt = self.tail
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if key in hashmap,
        # we try removing it first
        # then, we insert a new node with Node(key, value)
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        node = Node(key, value)
        self.insert(node)
        self.hashmap[key] = node
        if len(self.hashmap) > self.capacity:
            # if capacity exceeds, we remove node at head
            deletedNode = self.head.next
            self.remove(deletedNode)
            del self.hashmap[deletedNode.key]
                

        
