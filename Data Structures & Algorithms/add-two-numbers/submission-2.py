# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # return new linked list representing sum of two numbers
        # l1 and l2 have the same length
        a = b = 0
        i = 0
        while l1:
            a += l1.val * (10 ** i)
            l1 = l1.next
            i += 1
        i = 0
        while l2:
            b += l2.val * (10 ** i)
            l2 = l2.next
            i += 1
        c = a + b
        head = ListNode() # dummy node
        curr = head
        if c == 0:
            return ListNode()
        while c > 0:
            d = c % 10
            c //= 10
            curr.next = ListNode(d)
            curr = curr.next
        return head.next
