# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        answer = cur = head
        
        n = 0
        while cur:
            n += 1
            cur = cur.next
        
        mid  = math.floor(n/2) + 1

        for i in range(mid - 1):

            answer = answer.next
            
        return answer