# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0        
    
        def dfsHeight(node):
            nonlocal maxDiameter
            if not node:
                return 0
            left = dfsHeight(node.left)
            right = dfsHeight(node.right)

            maxDiameter = max(maxDiameter, left + right)
            return 1 + max(left, right)

        dfsHeight(root) 
        return maxDiameter