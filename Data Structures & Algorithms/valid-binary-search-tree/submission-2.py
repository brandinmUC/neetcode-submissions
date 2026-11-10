# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, upper, lower):
            if not node:
                return True
            
            if node.val >= upper or lower >= node.val:
                return False

            return dfs(node.left, node.val, lower) and dfs(node.right, upper, node.val)

        return dfs(root, math.inf, -math.inf)
            