# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        l = r = head
        while l.next and r.next and r.next.next:
            l = l.next
            r = r.next.next
            if l.val == r.val:
                return True
        return False

        