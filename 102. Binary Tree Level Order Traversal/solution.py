# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        first = root
        answer = []
        q  = [[first, 0]]
        
        group = []
        currlevel = 0
        
        if not first:
            return answer
        
        while q:
            
            curr, level = q.pop(0)
            
            if currlevel == level:
                group.append(curr.val)
            else:
                answer.append(group)
                group = []
                group.append(curr.val)
                currlevel = level
            
            #print(group)
            nextlevel = level + 1
            
            if curr.left:
                q.append([curr.left, nextlevel])
            if curr.right:
                q.append([curr.right, nextlevel])            
            
        if len(group) > 0:
            answer.append(group)
        
        return answer