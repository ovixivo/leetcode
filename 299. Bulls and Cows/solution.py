class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        x = 0 
        y = 0
        sList = list(secret)
        gList = list(guess)
        for i in range(len(sList)):
            if sList[i] == gList[i]:
                x += 1
                gList[i] = 'x'
                sList[i] = 'x'
                
        for i in range(len(sList)):
            if sList[i] == 'x':
                continue
            if sList[i] in gList:
                index = gList.index(sList[i])
                gList.pop(index)
                y += 1



        return f'{x}A{y}B'
                