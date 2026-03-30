# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # prev, curr
        # connect prev to curr.next when n reached
        # brute force: count length of linked list
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        
        k = length - n # true index of node to remove

        if k == 0:
            return head.next

        prev = None
        curr = head

        while k > 0:
            prev = curr
            curr = curr.next
            k -= 1

        # k == 0
        prev.next = curr.next
        curr = curr.next
        return head



        