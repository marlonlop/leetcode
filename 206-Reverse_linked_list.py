# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # iteratively
        prev = None
        
        while head:
            next_tmp = head.next
            head.next = prev
            prev = head
            head = next_tmp
        
        return prev

        '''
        # recursively O(n) S(n)
        if not head or not head.next:
            return head

        reversed_list_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return reversed_list_head
        '''