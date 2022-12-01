class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        

        answer = []
        pLen = len(p)
        i = 0
        j = pLen-1

        pCounter = Counter(p)
        sCounter = Counter(s[0:pLen])

        #print(pCounter,sCounter)
        
        while True:
            
            #print(pCounter, sCounter, pCounter == sCounter)
            if pCounter == sCounter:
                answer.append(i)
            
            if s[i] in sCounter:
                sCounter[s[i]] -= 1
            
            i += 1
            j += 1
            
            if j >= len(s):
                break
            
            sCounter[s[j]] += 1
            
        return answer
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# Slow with a lot patching        
#        answer = []     
#        if len(p) > len(s):
#            return answer
#        
#        if len(p) == 1:
#            for i in range(len(s)):
#                if p == s[i]:
#                    answer.append(i)
#            return answer
#               
#        counterP = Counter(p)
#        lenP = len(p)
#        
#        i = 0 
#        while i < len(s):
#            a = s[i:i + lenP]
#            if len(a) < lenP:
#                break
#            counterA = Counter(a)
#            if counterA == counterP:
#                answer.append(i)
#                answer, i = self.continueSearch(answer, s, i, lenP)
#                #print(answer, i)
# 
#            i += 1
#        
#        return answer
#    
#    def continueSearch(self, answer, s, i, lenP):
#        
#        nextIdx = i+lenP
#
#        if nextIdx >= len(s):
#            return answer, i
#        start = s[i]
#        nextChar = s[i+lenP]
#        #print(start,nextChar,i)
#        if start == nextChar and i not in answer:
#            answer.append(i)
#            answer, i = self.continueSearch(answer, s, i + 1, lenP)
#        
#        if start != nextChar:
#            i = i+lenP -2
#            #print(i)
#        return answer, i
        
        
        
## Slow Time limit Exceed        
#        answer = []     
#        if len(p) > len(s):
#            return answer
#        
#        counterP = Counter(p)
#        lenP = len(p)
#        for i in range(len(s)):            
#            a = s[i:i + lenP]
#            if len(a) < lenP:
#                break
#            counterA = Counter(a)
#            if counterA == counterP:
#                answer.append(i)
#        return answer