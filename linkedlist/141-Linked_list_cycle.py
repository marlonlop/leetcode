# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast:
            slow = slow.next 
            fast = fast.next if fast.next else None
            if fast:
                fast = fast.next if fast.next else None

            if slow == fast and fast:
                return True
        
        return False

    # shorter code
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False