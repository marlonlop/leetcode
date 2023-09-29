# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = root.val

        def dfsSum(node):
            if not node:
                return 0
            
            nonlocal max_path_sum
            max_left = dfsSum(node.left)
            max_right = dfsSum(node.right)
            max_left = max(max_left, 0)
            max_right = max(max_right, 0)

            # compact, less readable
            # max_left = max(dfsSum(node.left), 0)
            # max_right = max(dfsSum(node.right), 0)

            # max path seen so far
            max_path_sum = max(max_path_sum, node.val + max_left + max_right)

            return node.val + max(max_left, max_right)
        
        dfsSum(root)
        return max_path_sum