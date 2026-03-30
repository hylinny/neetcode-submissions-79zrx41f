# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # check current node. if both p and q are less than node, we go left
        # if both are greater than node, we go right
        # else if they split at this stage, we return current node output
        def check(node):
            if p.val < node.val and q.val < node.val:
                return check(node.left)
            elif p.val > node.val and q.val > node.val:
                return check(node.right)
            else: # p and q split at this stage, or one of the equals node val
                return node
        return check(root)
        