# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node, dep):
            if node is None: return
            
            if len(res) == dep: 
                res.append([])

            res[dep].append(node.val)
            
            dfs(node.left, dep+1)
            dfs(node.right, dep+1)
           
            

        dfs(root, 0)

        return len(res)