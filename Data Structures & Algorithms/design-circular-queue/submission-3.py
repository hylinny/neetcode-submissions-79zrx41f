class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.k = k
        self.head = ListNode() # dummy head

    def enQueue(self, value: int) -> bool:
        if self.capacity == 0:
            return False
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(value)
        self.capacity -= 1
        return True

    def deQueue(self) -> bool:
        if self.capacity == self.k:
            return False
        self.head.next = self.head.next.next
        self.capacity += 1
        return True

    def Front(self) -> int:
        if self.capacity == self.k:
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.capacity == self.k:
            return -1
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr.val

    def isEmpty(self) -> bool:
        return self.capacity == self.k

    def isFull(self) -> bool:
        return self.capacity == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()