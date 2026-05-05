# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        curr = head
        prev = None
        while index < left:
            prev = curr
            curr = curr.next
            index += 1
        tail = curr
        p = prev
        for _ in range(index, right+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # curr is now the new head
        tail.next = nxt
        if p:
            p.next = prev
            return head
        else:
            return prev
        # 1 -> 2 -> 3, left=2, right=3
