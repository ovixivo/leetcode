class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {}
        mapping["I"] = 1
        mapping["IV"] = 4
        mapping["V"] = 5
        mapping["IX"] = 9
        mapping["X"] = 10
        mapping["XL"] = 40
        mapping["L"] = 50
        mapping["XC"] = 90
        mapping["C"] = 100
        mapping["CD"] = 400
        mapping["D"] = 500
        mapping["CM"] = 900
        mapping["M"] = 1000
        
        order = ['M', 'CM', 'D', "CD", 'C', "XC", 'L', "XL", 'X', "IX", 'V', "IV", 'I']

        answer = ''
        for i in order:
            j = num // mapping[i]

            if j != 0:
                for k in range(j):
                    answer += i
                num -= j * mapping[i] 
            
        return answer