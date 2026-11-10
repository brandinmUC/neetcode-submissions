# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = self.generateNodePath(root, p, [root])
        q_path = set(self.generateNodePath(root, q, [root]))
        res = []

        for node in p_path:
            if node in q_path:
                res.append(node)
        return res[-1]


    def generateNodePath(self, root, node, path):  
        if not root:
            return None

        if node.val == root.val:
            return path
            
        l = self.generateNodePath(root.left, node, path + [root.left])
        r = self.generateNodePath(root.right, node, path + [root.right])

        return l if l else r
