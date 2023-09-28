# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True 
        if not root: return False

        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
                

    def isSameTree(self, subTreeA, subTreeB):
        if not subTreeA and not subTreeB:
            return True
        if not subTreeA or not subTreeB or subTreeA.val != subTreeB.val:
            return False
        return (self.isSameTree(subTreeA.left, subTreeB.left) and 
                self.isSameTree(subTreeA.right, subTreeB.right))