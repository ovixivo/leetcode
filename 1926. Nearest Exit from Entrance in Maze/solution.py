class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        #border
        m, n = len(maze), len(maze[0])
        
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        
        maze[entrance[0]][entrance[1]] = '+'
        
        q = [[entrance[0], entrance[1], 0]]
        
        while q:
            
            xo, yo, step = q.pop(0)
            
            if [xo, yo] != entrance and ((xo == 0 or xo == m-1) or (yo == 0 or yo == n-1)):
                return step
            
            
            for dx, dy in directions:
                a = [0, 0, 0]
                
                a[0] = xo + dx
                a[1] = yo + dy
                a[2] = step + 1
                
                if 0<=a[0]<m and 0<=a[1]<n and maze[a[0]][a[1]] == '.':
                    maze[a[0]][a[1]] = '+'
                    q.append(a)
                    
            
        
        return -1