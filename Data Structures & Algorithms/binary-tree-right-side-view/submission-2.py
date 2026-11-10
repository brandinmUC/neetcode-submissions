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
                # print(q)
                first = q.pop()
                rem = []
                if first:
                    res.append(first.val)
                    while q:
                        x = q.popleft() # all the nodes before the rightmost on that level
                        if x:
                            rem.append(x) 
                else:
                    break
                if rem:
                    # print(rem)
                    for node in rem:
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
                if first.left:
                    q.append(first.left)
                if first.right:
                    q.append(first.right)

            return res
