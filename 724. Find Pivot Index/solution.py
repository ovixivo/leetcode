class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumleft = 0 
        sumright = sum(nums)
        
        answer = -1
        for i in range(len(nums)):
            sumright -= nums[i]
            if sumleft == sumright:
                answer = i
                break
            else:
                sumleft += nums[i]
                
        return answer