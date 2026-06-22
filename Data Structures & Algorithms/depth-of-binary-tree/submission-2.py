# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        stack = [[root, 1]]
        maxd = 0

        while stack:
            node, dep = stack.pop()
            maxd = max(maxd, dep)
            if node.left:
                stack.append([node.left, dep+1])
            if node.right:
                stack.append([node.right, dep+1])

        return maxd
        