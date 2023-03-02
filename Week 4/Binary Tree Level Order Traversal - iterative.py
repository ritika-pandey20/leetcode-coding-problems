
0/5
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #iterative - Time = O(n) Space = O(n)
        res = []
        if not root:
            return res
        level = 0
        queue = deque([root,])
        while queue:
            res.append([])
            tot_level = len(queue)

            for i in range(tot_level):
                node = queue.popleft()
                res[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level +=1