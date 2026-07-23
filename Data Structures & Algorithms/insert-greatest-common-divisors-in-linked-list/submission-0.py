# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while a % b != 0:
                # a = pb + r
                a, b = b, a % b
            return b
        curr = head
        while curr.next:
            nxt = curr.next
            newVal = gcd(curr.val, nxt.val)
            node = ListNode(newVal, nxt)
            curr.next = node
            curr = curr.next.next
        return head