# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if(root is None):
            return max_depth
        queue = [root]
        while(queue):
            max_depth += 1
            for i in range(len(queue)):
                root = queue.pop(0)
                if(root.left):
                    queue.append(root.left)
                if(root.right):
                    queue.append(root.right)
        return max_depth
