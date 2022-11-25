"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        curr = root
        output = []
               
        def dfs(curr):
            #print (output)
            if curr:
                output.append(curr.val)
                
                for child in curr.children:
                    dfs(child)
        
        dfs(curr)
        return output