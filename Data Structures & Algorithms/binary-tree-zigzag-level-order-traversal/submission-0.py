# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # left to right queue
        # right to left array
        queue = deque()
        queue.append(root)
        level = 0
        output = []
        while queue:
            current = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                current.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 != 0:
                current.reverse()
            output.append(current)
            level += 1
        return output

