# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        sequence = []
        def dfs(node):
            if not node:
                sequence.append('#')
                return
            sequence.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ' '.join(sequence)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        sequence = data.split(' ')
        i = 0
        def dfs():
            nonlocal i
            if i >= len(sequence):
                return None
            value = sequence[i]
            if value == '#':
                i += 1
                return None
            node = TreeNode(int(value))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        