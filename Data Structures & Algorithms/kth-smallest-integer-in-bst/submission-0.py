# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursive solution
        def inorder(node):
            nonlocal k
            if not node:
                return -1
            truthy = inorder(node.left)
            if truthy != -1:
                return truthy
            k -= 1
            if k == 0:
                return node.val
            truthy = inorder(node.right)
            if truthy != -1:
                return truthy
            return -1
        return inorder(root)