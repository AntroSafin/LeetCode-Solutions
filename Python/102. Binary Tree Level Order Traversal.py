# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        queue = [root]
        while(queue):
            level = []
            for i in range(len(queue)): 
                root = queue.pop(0)
                level.append(root.val)
                if(root.left):
                    queue.append(root.left)
                if(root.right):
                    queue.append(root.right)
            ans.append(level)
        return ans
