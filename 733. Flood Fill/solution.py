class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        
        m, n = len(image), len(image[0])
        
        startValue = image[sr][sc]
        
        if startValue == color:
            return image
        
        image[sr][sc] = color
        
        q = [[sr,sc]]
        
        while q:
            
            xo, yo = q.pop(0)
            
            for dx, dy in directions:
                a = [0, 0]
                
                a[0] = xo + dx
                a[1] = yo + dy

                
                if 0<=a[0]<m and 0<=a[1]<n and image[a[0]][a[1]] == startValue:
                    image[a[0]][a[1]] = color
                    q.append(a)
        
        return image