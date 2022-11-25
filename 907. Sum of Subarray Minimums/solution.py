
##Monotonic Stack

## Find number of sub array the current value is smallest in 
## the number of subarrays = (index - left) * (right - index)

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        m = 10**9 + 7
        
        #Create an index list for max right boundary (after last element)
        leftToRight = [len(arr)] * len(arr)

        stack = []

        #For each value, find the index of the closest smaller number to the right
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                leftToRight[stack.pop()] = i
            stack.append(i)
        #print(leftToRight)
        
        #Create an index list for max left boundary (before first element)
        rightToLeft = [-1] * len(arr)
        
        stack = []
        
        #For each value, find the index of the closest smaller number to the left
        for i in reversed(range(len(arr))):
            while stack and arr[i] < arr[stack[-1]]:
                rightToLeft[stack.pop()] = i
            stack.append(i)
        #print(rightToLeft)    
        
        res = 0
        
        for idx in range(len(arr)):
            l, r = rightToLeft[idx], leftToRight[idx]
            
            ## Formula for number of sub array curent value is smallest in (r-idx) * (idx-l) 
            res += (r-idx) * (idx-l) * arr[idx]
            res %= m
        
        return res
            
  
            
# Solution too slow, cannot handle large array            
#        m = 10**9 + 7
#        
#        subarr = self.sub_lists(arr)
#        subarr.pop(0)
#        
#        answer = 0
#        for item in subarr:
#            answer += min(item)
#
#        return answer%m
#        
#    def sub_lists (self, l):
#        lists = [[]]
#        for i in range(len(l) + 1):
#            for j in range(i):
#                lists.append(l[j: i])
#        return lists