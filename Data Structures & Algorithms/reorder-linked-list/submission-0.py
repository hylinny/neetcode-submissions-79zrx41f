# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # even n=4: 0, (n-1)3, 1, (n-2)2
        # odd n=5: 0, (n-1)4, 1, (n-2)3, 2
        # iterate through all nodes and store in list
        # two pointer approach: grab left increment left grab right decrement right
        # stop in the middle after left if odd

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        dummy = ListNode()
        curr = dummy
        
        left, right = 0, len(nodes)-1
        while left <= right:
            curr.next = nodes[left]
            curr = curr.next
            left += 1
            if left > right:
                break
            curr.next = nodes[right]
            curr = curr.next
            right -= 1
        curr.next = None

        