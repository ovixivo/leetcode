class Solution:
    def reverse(self, x: int) -> int:

        neg = False
        if x < 0:
            neg = True
            x = int(str(x)[1:])
        
        rev = int(str(x)[::-1])

        if neg:
            rev = rev * -1

        return 0 if rev<-2**31 or rev>2**31-1 else rev