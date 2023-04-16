# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1q = deque()
        while l1:
            l1q.appendleft(l1.val)
            l1 = l1.next

        l2q = deque()
        while l2:
            l2q.appendleft(l2.val)
            l2 = l2.next

        l1num = int(''.join([str(x) for x in l1q]))
        l2num = int(''.join([str(x) for x in l2q]))
        
        answernum = str(l1num + l2num)[::-1]

        answer = ListNode(answernum[0])
        curr = answer
        i = 1
        while (i < len(answernum)):
            curr.next = ListNode(answernum[i])
            curr = curr.next
            i += 1

        return answer