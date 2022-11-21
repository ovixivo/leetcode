class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        tList = list(t)
        
        start = 0
        for char in s:
            print(start)
            try:
                start = tList.index(char, start) + 1
            except ValueError:
                return False
        
        return True