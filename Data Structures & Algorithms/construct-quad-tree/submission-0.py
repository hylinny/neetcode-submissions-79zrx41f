"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # divide and conquer
        # reach base level, return 4 nodes
        # if val of all 4 nodes are the same, 
        # we combine and return a unified leaf node
        # otherwise, create a new node, set its 4 children,
        # and return
        def buildTree(top, left, size):
            if size == 1:
                return Node(grid[top][left], True)
            topLeft = buildTree(top, left, size // 2)
            topRight = buildTree(top, left + size // 2, size // 2)
            bottomLeft = buildTree(top + size // 2, left, size // 2)
            bottomRight = buildTree(top + size // 2, left + size // 2, size // 2)
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, True)
            else:
                return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        return buildTree(0, 0, len(grid))

        