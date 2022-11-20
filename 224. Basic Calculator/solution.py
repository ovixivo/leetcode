class Solution:
    def calculate(self, s: str) -> int:
        
        s = s.replace(' ', '')
        s = '(' + s + ')'
        
        multiplier = 1
        prevMultiplier = 1
        total = 0
        digit = 0
        currentSum = 0
        vStack = []
        sStack = []
        digiBox = ['0']
        
        for char in s:
            if char in '-+()':
                
                if char == '-':
                    multiplier = -1
                elif char == '+':
                    multiplier = 1
                elif char == '(':
                    vStack.append(currentSum)
                    sStack.append(prevMultiplier)
                    currentSum = 0
                    multiplier = 1

                elif char == ')':
                    digit = "".join(digiBox)
                    digiBox = ['0']
                    currentSum += prevMultiplier * int(digit)
                    #print(f'char: {char} \t currentSum: {currentSum}')
                    currentSum = vStack[-1] + sStack[-1] * currentSum
                    vStack.pop()
                    sStack.pop()
                    #print(f'char: {char} \t currentSum: {currentSum} \t vStack: {vStack} \t sStack: {sStack}')
                    continue
                
                digit = "".join(digiBox)
                digiBox = ['0']
                currentSum += prevMultiplier * int(digit)
                
                
            else:
                digiBox.append(char)
                
            prevMultiplier = multiplier
        
            #print(f'char: {char} \t currentSum: {currentSum} \t vStack: {vStack} \t sStack: {sStack}')
        return currentSum