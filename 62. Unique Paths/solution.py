class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache #without this time limit will exceed
        def dfs(i, j):
            #print(i, j)
            if i >= m or j >=n:
                return 0
            
            if i == m -1 and j == n - 1:
                return 1
            
            return dfs(i + 1, j) + dfs(i, j + 1)
        
        return dfs(0,0)