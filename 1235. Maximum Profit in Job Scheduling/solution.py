class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        
        
        jobList = sorted(zip(startTime, endTime, profit))
        n = len(startTime)
        
        dp = [0] * (n + 1) 
        
        #print(jobList)
        for i in reversed(range(n)):
            
            #Find the index of the closest previous ending job
            #key is selecting what to compare
            #bisect_left return index of where to insert the element softed order
            k = bisect_left(jobList, jobList[i][1], key=lambda j: j[0])
            #Calculate the highest profit (from the back)
            dp[i] = max(jobList[i][2] + dp[k], dp[i+1])
            #print(k,jobList[i][1], dp)

        return dp[0]