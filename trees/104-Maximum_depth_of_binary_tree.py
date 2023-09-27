# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS iteratively (Pre-order)
        if not root:
            return 0
        
        stack = [[root, 1]]
        h = 0
        while stack:
            node, depth = stack.pop()
            if node.right:
                stack.append([node.right, depth + 1])
            if node.left:
                stack.append([node.left, depth + 1])
            h = max (h, depth)
        return h

    """
    # BFS iteratively
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        height = 0
        q = deque([root])
        while q:
            cur_length = len(q)
            for el in range(cur_length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            height += 1
        return height
    """
    '''
    # DFS recursively
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    '''