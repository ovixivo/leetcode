# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #print(root)
        
        leftLimit = -math.inf
        rightLimit = math.inf
        rootValue = root.val
        
        return self.dfs(root, leftLimit, rightLimit)
        
    def dfs(self, curr, leftLimit, rightLimit):
        
        if not curr:
            return True

        currValue = curr.val
        if not (currValue > leftLimit and currValue < rightLimit):
            return False
        
        return self.dfs(curr.left, leftLimit, currValue) and self.dfs(curr.right, currValue, rightLimit) 
        
            