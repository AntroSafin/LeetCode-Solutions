# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if(root is None):
            return True
        def Symmetric(root1,root2):
            if(root1 and root2):
                return (root1.val == root2.val) and Symmetric(root1.left,root2.right) and Symmetric(root1.right,root2.left)
            return root1 == root2
        return Symmetric(root.left,root.right)
