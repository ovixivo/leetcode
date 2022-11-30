class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        aDict = {}
        aDict = defaultdict(lambda:0,aDict)
        
        for i in arr:
            aDict[i] += 1
        
        aSet = set()
        for k, v in aDict.items():
            if v in aSet:
                return False
            else:
                aSet.add(v)
        return True