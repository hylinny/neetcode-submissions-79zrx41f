# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        def dfs(node):
            if not node:
                return None
            if node.val == target and not node.left and not node.right:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
        for i in range(getHeight(root)):
            dfs(root)
        if root.val == target and not root.left and not root.right:
            return root.left # return null value, pick either
        return root
        