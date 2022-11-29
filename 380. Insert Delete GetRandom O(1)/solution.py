class RandomizedSet:

    def __init__(self):
        self.rIndex = {}
        self.rList= []

    def insert(self, val: int) -> bool:
        if val in self.rIndex:
            return False
        else:
            self.rList.append(val)
            self.rIndex[val] = len(self.rList) - 1
            return True

    #Only by list.pop() last element then O(1)
    def remove(self, val: int) -> bool:
        if val in self.rIndex:
            i = self.rIndex[val]
            
            #Change switch last element postion, replacing element to remove
            self.rIndex[self.rList[-1]] = i
            self.rList[i] = self.rList[-1]
            
            self.rIndex.pop(val)
            self.rList.pop()

            return True
        else:
            return False      

    def getRandom(self) -> int:
        return random.choice(self.rList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


## random.choice(tuple(self.rSet)) is not O(1)
#    def __init__(self):
#        self.rSet = set()
#
#    def insert(self, val: int) -> bool:
#        if val in self.rSet:
#            return False
#        else:
#            self.rSet.add(val)
#            return True
#
#    def remove(self, val: int) -> bool:
#        if val in self.rSet:
#            self.rSet.remove(val)   
#            return True
#        else:
#            return False      
#
#    def getRandom(self) -> int:
#        return random.choice(tuple(self.rSet))