# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # at current step, we can either choose to take node 
        # value and flip boolean, or choose not to take node
        # and keep boolean
        dp = {}
        def dfs(node, rob):
            if (node, rob) in dp:
                return dp[(node, rob)]
            if not node:
                return 0
            left = dfs(node.left, not rob)
            right = dfs(node.right, not rob)
            if not rob:
                dp[(node, rob)] = left + right
            else:
                dp[(node, rob)] = max(
                    node.val + left + right,
                    dfs(node.left, rob) + dfs(node.right, rob)
                )
            return dp[(node, rob)]
        return dfs(root, True)