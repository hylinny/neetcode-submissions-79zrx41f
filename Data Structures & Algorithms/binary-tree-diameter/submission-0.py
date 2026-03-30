# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxHeight = 0
        def dfs(node):
            nonlocal maxHeight
            if not node:
                return 0
            # grab left and right subtree's values
            currentMax = 0
            left = dfs(node.left)
            right = dfs(node.right)
            currentMax = left + right
            maxHeight = max(maxHeight, currentMax)
            return 1 + max(left, right)
        dfs(root)
        return maxHeight