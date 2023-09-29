# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validHelper(node, l_bound, r_bound):
            if not node:
                return True
            # if not (node.val > l_bound and node.val < r_bound):
            #     return False
            if not l_bound < node.val < r_bound:
                return False
            
            return (validHelper(node.left, l_bound, node.val) and
                    validHelper(node.right, node.val, r_bound))
        
        return validHelper(root, float("-inf"), float("inf"))