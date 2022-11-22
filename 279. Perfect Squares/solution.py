###
### There can only be 4 answer due to math

###    k = 1: Ruud's One-Square Theorem
###    k = 2: Fermat's Two-Square Theorem
###    k = 3: Legendre's Three-Square Theorem
###    k = 4: Lagrange's Four-Square Theorem

from math import isqrt

class Solution:
    def numSquares(self, n: int) -> int:
        
        #Ruud's One-Square Theorem - the value is a square
        if isqrt(n)**2 == n:
            return 1
        
        #Fermat's Two-Square Theorem - check if it is made up of 2 squares
        for i in range(1, isqrt(n)+1):
            leftover = n - i**2
            if isqrt(leftover)**2 == leftover:
                return 2
        
        #Legendre's Three-Square Theorem 
        #Legendre's three-square theorem states that a natural number can be represented as the sum of three squares of integers if and only if n is not of the form : n = 4a (8b+7), for non-negative integers a and b
        while n%4 == 0:
            n = n/4
        if n % 8 != 7:
            return 3   
        
        #Lagrange's Four-Square Theorem
        #Lagrange's four-square theorem, also known as Bachet's conjecture, states that every natural number can be represented as the sum of four integer squares.
        return 4
            
 