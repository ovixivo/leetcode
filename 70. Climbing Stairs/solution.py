class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0, 1, 2]
        
        if n <= 2:
            return n
        
        while len(f) < n:
            
            i = f[-1]
            j = f[-2]
            
            f.append(i + j)
            
        #print(f, n, n-1, n-2)
        return (f[n-1] + f[n-2])