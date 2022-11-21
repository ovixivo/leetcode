class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        wordDict = {}
        for i in range(len(s)):
            
            if s[i] in wordDict:
                if wordDict[s[i]] != t[i]:
                    return False
            else:
                wordDict[s[i]] = t[i] 
        
        wordSet = set()
        for key, value in wordDict.items():
            wordSet.add(value)
        
        if len(wordSet) == len(wordDict):
            return True
        else:
            return False