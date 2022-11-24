class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        
        startList = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                if board[i][j] == word[0]:
                    startList.append([i, j])
        
        if len(startList) == 0:
            return False
        
        print(startList)
        for start in startList:
            xo, yo = start[0], start[1]
            charIndex = 0
            
            if self.dfs(board, word, xo, yo, charIndex):
                return True
        return False
            
    
    def dfs(self, board, word, x, y, charIndex):
        
        m, n = len(board), len(board[0])
        if charIndex == len(word):
            return True
        
        
        if 0<=x<m and 0<=y<n and board[x][y] == word[charIndex]:
            #print(board[x][y], charIndex, word[charIndex])
            board[x][y] = '.'
            a = self.dfs(board, word, x + 1, y, charIndex + 1)
            b = self.dfs(board, word, x - 1, y, charIndex + 1)
            c = self.dfs(board, word, x, y + 1, charIndex + 1)
            d = self.dfs(board, word, x, y - 1, charIndex + 1)
            board[x][y] = word[charIndex]
            return a or b or c or d
        
        else:
            return False

            
                