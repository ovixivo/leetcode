# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


## Floyd’s Cycle Finding Algorithm
## While traversing the linked list one of these things will occur-
##
##    The Fast pointer may reach the end (NULL) this shows that there is no loop in the linked list.
##    The Fast pointer again catches the slow pointer at some time therefore a loop exists in the linked list.

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                slow = head
                
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow
        
        return None
        
        