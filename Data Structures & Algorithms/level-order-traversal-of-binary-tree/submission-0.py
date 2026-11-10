# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        q = deque([[root]])
        seen = set()

        while q:
            # print(q)
            lvl_val = []
            lvl_nodes = []
            node_lst = q.popleft()
            for node in node_lst:
                if node not in seen:
                    seen.add(node)
                    lvl_val.append(node.val)
                    if node.left:
                        lvl_nodes.append(node.left)
                    if node.right:
                        lvl_nodes.append(node.right)
                    if lvl_nodes:
                        q.append(lvl_nodes)
            if lvl_val:
                res.append(lvl_val)
            # print(lvl_val, lvl_nodes)
        return res
