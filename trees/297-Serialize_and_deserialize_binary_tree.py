# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        out = []
        def dfs(node):
            if not node:
                out.append("N")    
                return 
            
            out.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return "|".join(out)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        inpt = data.split("|")
        i = 0
        def dfsBuild():
            nonlocal i
            if inpt[i] == "N":
                i += 1
                return None            
            node = TreeNode(int(inpt[i]))
            i += 1
            node.left = dfsBuild()
            node.right = dfsBuild()
            return node
        return dfsBuild()



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))