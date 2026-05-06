# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1
        n //= k
        # reverse k nodes n times
        prev = None
        curr = head
        dummy = ListNode()
        dummy.next = head
        prevEnd = dummy
        for i in range(n):
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            # prev = 3, curr = 4, head = 1, prevEnd = dummy
            prevEnd.next = prev
            prevEnd = head
            head.next = curr
            prev = head
            head = head.next # head = 4, prev = 1
        return dummy.next