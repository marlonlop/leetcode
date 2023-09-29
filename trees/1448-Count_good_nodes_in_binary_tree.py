# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs( node, maxVal):
            if not node:
                return 0
            # upd count and and check new max value
            gd_nodes_cnt = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            
            gd_nodes_cnt += dfs(node.left, maxVal)
            gd_nodes_cnt += dfs(node.right, maxVal)
            return gd_nodes_cnt

        return dfs(root, root.val)
    
    '''
        # version using nonlocal
        # could also remove self. and uncomment nonlocal
        
        def goodNodes(self, root: TreeNode) -> int:
        self.gd_nodes_cnt = 0

        def dfs( node, maxVal):
            if not node:
                return 0
            #nonlocal gd_nodes_cnt

            self.gd_nodes_cnt += 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
            
            #return gd_nodes_cnt
        
        dfs(root, root.val)
        return self.gd_nodes_cnt

    '''