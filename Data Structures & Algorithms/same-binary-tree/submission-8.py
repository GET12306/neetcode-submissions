# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1 = self.inorder(p)
        res2 = self.inorder(q)
        print(res1)
        print(res2)

        return res1 == res2

    
    def inorder(self, node) -> list:
        res = []

        def dfs(node):
            if not node: 
                res.append(None)
                return
            
            if not node.left and not node.right:
                res.append(node.val)
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(node)
        return res
