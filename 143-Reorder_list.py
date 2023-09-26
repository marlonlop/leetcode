# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find start of second half of list
        slowP, fastP = head, head.next
        while fastP and fastP.next:
            slowP, fastP = slowP.next, fastP.next.next
        
        # reverse second half of list
        reversedHead = slowP.next
        prev = slowP.next = None
        while reversedHead:
            next_tmp = reversedHead.next
            reversedHead.next = prev
            prev = reversedHead
            reversedHead = next_tmp
        mid = slow
        
        ''' by upcaking there is no need to keep track of next_temp
        # Reverse second half
        prev, cur = None, mid
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        head_of_second_rev = prev
        '''

        # merge
        firstH, secondH = head, prev
        while secondH:
            tmp1, tmp2 = firstH.next, secondH.next
            firstH.next = secondH
            secondH.next = tmp1
            firstH, secondH = tmp1, tmp2
      
#1 5 2,3 4 n      
