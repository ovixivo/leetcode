class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        for horList in board:     
            #print('horList', horList)
            checkH = {i:horList.count(i) for i in horList}
            checkH.pop('.',None)            
            for k, v in checkH.items():
                if v > 1:
                    return False

        for i in range(0, 9):
            verList = []
            for j in range(0, 9):
                verList.append(board[j][i])
              
            #print('verList', verList)
            checkV = {i:verList.count(i) for i in verList}
            checkV.pop('.',None)
            for k, v in checkV.items():
                if v > 1:
                    return False
                


        hStart = 0
        hEnd = 2
        vStart = 0
        vEnd = 2
        
        endFlag = False
        while not endFlag:
            groupList = []
            for i in range(hStart, hEnd+1):
                for j in range(vStart, vEnd+1):
                    groupList.append(board[i][j])   
                    
            #print('groupList', groupList)
            checkG = {i:groupList.count(i) for i in groupList}
            checkG.pop('.',None)
            
            for k, v in checkG.items():
                if v > 1:
                    return False
            
            if vEnd != 8:
                vStart += 3
                vEnd += 3
            else:
                hStart += 3
                hEnd += 3
                vStart = 0
                vEnd = 2
                
            if hEnd > 8:
                endFlag = True
        
        return True