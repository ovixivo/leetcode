class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        
        total = 0
        for i in nums:
            total += i
            answer.append(total)
        
        return answer