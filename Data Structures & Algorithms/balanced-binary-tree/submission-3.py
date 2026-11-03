# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]

            l, r = dfs(node.left), dfs(node.right)
            if abs(l[1] - r[1]) <= 1 and l[0] and r[0]:
                res = [True, 1 + max(l[1], r[1])]
            else:
                res = [False, 1 + max(l[1], r[1])]
            return res

        return dfs(root)[0]
