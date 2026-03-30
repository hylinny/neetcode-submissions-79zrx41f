# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # for each path down the tree,
        # keep track of largest node value found so far
        # passed in as a parameter to the dfs function
        counter = 0
        def dfs(node, value):
            nonlocal counter
            if not node:
                return
            if node.val >= value:
                # current node largest so far
                counter += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            else:
                # value found larger than current node
                dfs(node.left, value)
                dfs(node.right, value)
        dfs(root, root.val)
        return counter
            
        