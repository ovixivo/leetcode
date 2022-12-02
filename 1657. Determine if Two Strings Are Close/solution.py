class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        #print(counter1.keys(), counter2.keys(), counter1.keys() == counter2.keys())
        #print(sorted(counter1.values()), sorted(counter2.values()), sorted(counter1.values()) == sorted(counter2.values()))
        
        if counter1.keys() == counter2.keys() and sorted(counter1.values()) == sorted(counter2.values()):
            return True
        else:
            return False
        