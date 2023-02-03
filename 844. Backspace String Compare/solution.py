class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        i = 0
        j = 0
        
        sList = list(s)
        tList = list(t)
        
        while i < len(sList):
            #print(sList, i)

            if sList[i] == '#':
                if i == 0:
                    sList.pop(i)
                else:
                    sList.pop(i)
                    sList.pop(i-1)
                    i -= 1
            else:
                i += 1

        while j < len(tList):
            #print(tList,tList[j], j)
            
            if tList[j] == '#':
                if j == 0:
                    tList.pop(j)
                else:
                    tList.pop(j)
                    tList.pop(j-1)
                    j -= 1
            else:
                j += 1
        
        
        #print(sList, tList)
        return sList == tList