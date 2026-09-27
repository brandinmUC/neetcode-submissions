# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(p, q):
            if not p and not q:
                return True
            if (not p or not q) or (p.val != q.val):
                return False
            else:
                res1 = dfs(p.left, q.left)
                res2 = dfs(p.right, q.right)
            return res1 and res2
        return dfs(p, q)
                    
