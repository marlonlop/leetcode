"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        og_2_copy_map = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            og_2_copy_map[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = og_2_copy_map[curr]
            copy.val = curr.val
            copy.next = og_2_copy_map[curr.next]
            copy.random = og_2_copy_map[curr.random] 
            curr = curr.next
            
        return og_2_copy_map[head]
