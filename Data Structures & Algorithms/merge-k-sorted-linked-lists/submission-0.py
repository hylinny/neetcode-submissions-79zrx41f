# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for head in lists:
            curr = head
            while curr:
                arr.append(curr.val)
                curr = curr.next
        arr.sort()
        head = ListNode()
        curr = head
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return head.next
        