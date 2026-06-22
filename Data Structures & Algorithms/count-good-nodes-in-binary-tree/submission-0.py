# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, mvalue):
            nonlocal res
            if node is None: return
            if node.val >= mvalue:
                res += 1
                mvalue = node.val
            dfs(node.left, mvalue)
            dfs(node.right, mvalue)
        
        dfs(root, root.val)

        return res