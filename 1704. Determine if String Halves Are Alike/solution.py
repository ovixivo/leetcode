class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        vowels = set('aeiou')
        
        half = len(s)//2

        a = s[:half]
        b = s[half:]
        
        aC = Counter(a.lower())
        aCounter = sum(aC[v] for v in vowels)

        bC = Counter(b.lower())
        bCounter = sum(bC[v] for v in vowels)
        
        return aCounter == bCounter