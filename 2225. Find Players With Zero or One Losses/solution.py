class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        noLost = set()
        oneLost = set()
        manylost = set()
        
        for i in range(len(matches)):
            winner = matches[i][0]
            loser = matches[i][1]
            
            noLost.discard(loser)
            
            if winner not in oneLost and winner not in manylost:
                noLost.add(winner)
            
            if loser not in oneLost and loser not in manylost:
                oneLost.add(loser)
            elif loser in oneLost and loser not in manylost:
                oneLost.discard(loser)
                manylost.add(loser)
                

                
        answer = [sorted(list(noLost)), sorted(list(oneLost))]
        
        return answer