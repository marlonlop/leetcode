# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        tail = head
        r = dummy
        for i in range(n):
            tail = tail.next
            i += 1

        while tail:
            r = r.next
            tail = tail.next
        
        r.next = r.next.next
        return dummy.next
    
    
    