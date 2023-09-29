# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
           return None

        root = TreeNode(preorder[0])
        index = inorder.index(preorder.pop(0)) # i

        root.left = self.buildTree(preorder, inorder[:index]) #remainder of pre and all to the left of index[:i]
        root.right = self.buildTree(preorder, inorder[index + 1:])#remainder of pre and all to the rigth of inorder[i+1:]
        return root

'''
        start
        # p = [3,9,20,15,7] i = [9,3,15,20,7]
        pop 3 as root                                                                        3
        left
        # p = [9,20,15,7] i = [9] Left recur (everything left of index)
        pop 9 as root                                                           9
        # p = [20,15,7] i = [] 
        
        right
        pop 20 as root                                                                                20
        # p = [15,7] i = [7] rigth recur (everything right of index)
        left
        pop 15 as root                                                                          15
        # p = [7] i = [] 

        right 
        pop 7 as root                                                                                       7
        # p = [] i = [] 
'''