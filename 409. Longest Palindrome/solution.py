class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        palindrome = 0
        sDict = {}
        for char in s:
            
            if char not in sDict:
                sDict[char] = 1
            else:
                sDict.pop(char)
                palindrome += 2
        
        if sDict:
            palindrome += 1
        
        return palindrome