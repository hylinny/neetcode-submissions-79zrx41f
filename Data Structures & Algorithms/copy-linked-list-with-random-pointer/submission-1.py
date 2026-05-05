"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        def build(curr):
            if curr is None:
                return None
            node = Node(curr.val)
            node.next = build(curr.next)
            hashmap[curr] = node
            return node
        newhead = build(head)
        curr = newhead
        while head:
            rand = head.random
            if rand:
                curr.random = hashmap[rand]
            head = head.next
            curr = curr.next
        return newhead
            