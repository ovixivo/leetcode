class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {}
        mapping["I"] = 1
        mapping["V"] = 5
        mapping["X"] = 10
        mapping["L"] = 50
        mapping["C"] = 100
        mapping["D"] = 500
        mapping["M"] = 1000
        
        order = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        
        index = 0
        total = 0
        for char in s[::-1]:
            if index == 0:
                prevI = order.index(char)
                prevV = mapping[char]
                total += prevV
                index = 1
                
                print ("total", total)
                continue
                
            currI = order.index(char)
            currV = mapping[char]
            if currI <= prevI:
                total += currV
            else:
                total -= currV
                
            prevI = currI
            prevV = currV
            print ("total", total) 
        return total