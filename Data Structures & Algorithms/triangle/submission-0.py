class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # accumulate minimum path sum down the tree
        # treat it like a tree
        # base case: we reach depth > height of tree. just return 0.
        # recurrence: take the min of the left and right subtree, then add current
        # return the top
        height = len(triangle)
        dp = {}
        def recurse(m, n):
            if m == height:
                return 0
            if (m, n) in dp:
                return dp[(m, n)]
            leftChild = recurse(m+1, n)
            rightChild = recurse(m+1, n+1)
            dp[(m, n)] = triangle[m][n] + min(leftChild, rightChild)
            return dp[(m, n)]
        return recurse(0, 0)

        