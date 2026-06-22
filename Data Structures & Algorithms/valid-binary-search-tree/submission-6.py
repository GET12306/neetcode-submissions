# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append((root, -2000, 2000))

        while q:
            node, under, top = q.popleft()
            if not under < node.val < top:
                return False
            if node.left:
                q.append((node.left, under, node.val))
            if node.right:
                q.append((node.right, node.val, top))
        
        return True
