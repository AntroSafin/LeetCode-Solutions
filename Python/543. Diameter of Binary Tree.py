# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
        
    def depth(self,root):
        left = self.depth(root.left) if root.left else 0
        right = self.depth(root.right) if root.right else 0
        
        self.diameter =  max(self.diameter,left+right)
        return max(left,right) + 1
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.diameter
