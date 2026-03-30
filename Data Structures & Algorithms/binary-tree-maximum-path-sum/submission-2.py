# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # native solution:
        # iterate through all nodes, and assume path passes through
        # current node
        # for each current node, we compute maximum path sum
        # left side must be positive, right side must be +ve
        # to add to sum, else ignore either left / right side
        maxPath = float('-inf')
        def inorder(node):
            nonlocal maxPath
            if not node:
                return
            inorder(node.left)
            # process
            leftmax = max(0, path(node.left))
            rightmax = max(0, path(node.right))
            maxPath = max(maxPath, leftmax + rightmax + node.val)
            inorder(node.right)

        def path(node): # returns maximum path that passes through node
            if not node:
                return 0
            leftmax = max(0, path(node.left))
            rightmax = max(0, path(node.right))
            return max(leftmax + node.val, rightmax + node.val)
        inorder(root)
        return maxPath
            





