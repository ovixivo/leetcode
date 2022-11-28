class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        counter = 0
        for i in range(m):
            for j in range(n):     
                if grid[i][j] != '0':
                    counter += 1
                    self.dfs(grid, i, j)

        return counter
    
    def dfs(self, grid, xo, yo):
        
        m, n = len(grid), len(grid[0])
        
        
        if 0<=xo<m and 0<=yo<n and grid[xo][yo] != '0':
            grid[xo][yo] = '0'
            self.dfs(grid, xo + 1, yo)
            self.dfs(grid, xo - 1, yo)
            self.dfs(grid, xo, yo + 1)
            self.dfs(grid, xo, yo - 1)
            
        return