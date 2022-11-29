class Solution:
    def fib(self, n: int) -> int:
        
        f = [0, 1]
        
        if n < 2:
            return f[n]
        
        while len(f) < n:
            
            i = f[-1]
            j = f[-2]
            
            f.append(i +j)
            
        return (f[n-1] + f[n-2])
            