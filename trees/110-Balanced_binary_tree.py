# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            return 1 + max (dfs(node.left), dfs(node.right))
        
        if not root:
            return True

        left = dfs(root.left)
        right = dfs(root.right)

        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        # if abs(left - right) <= 1 or not left or not right:
        #     return False
        # return True # fails on one test case
        
"""
        [1,null,2,null,3]
                        1
                    n       2
                                3
                

                                    5
                            2               1
                        6       0       2       3
                    4                3           
                                1 

"""