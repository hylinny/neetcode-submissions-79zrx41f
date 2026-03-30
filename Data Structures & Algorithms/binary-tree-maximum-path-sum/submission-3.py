# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')

        def solve(node):
            nonlocal result
            if not node:
                return 0
            leftmax = max(0, solve(node.left))
            rightmax = max(0, solve(node.right))
            currmax = node.val + leftmax + rightmax # path passes through current node
            result = max(result, currmax)
            return node.val + max(leftmax, rightmax) # path does not pass through current node
        solve(root)
        return result

            





