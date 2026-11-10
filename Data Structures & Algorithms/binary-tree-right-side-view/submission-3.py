# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            res = []
            q = deque([root])

            while q:
                rightMost = None
                n = len(q)

                for i in range(n):
                    node = q.popleft()

                    if node:
                        rightMost = node
                        q.append(rightMost.left)
                        q.append(rightMost.right)
                
                if rightMost:
                    res.append(rightMost.val)

            return res
