# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p1 = deque([p])
        q1 = deque([q])

        while p1 and q1:
            for _ in range(len(p1)):
                np, nq = p1.popleft(), q1.popleft()
                if np is None and nq is None:
                    continue
                if np is None or nq is None or np.val!=nq.val:
                    return False
                p1.append(np.left)
                p1.append(np.right)
                q1.append(nq.left)
                q1.append(nq.right)
        return True
            
            
