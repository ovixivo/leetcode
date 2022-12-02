class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
                        
            diff = target - nums[i]
            
            try:
                index = nums.index(diff,i+1)
                return [i, index]
            except ValueError:
                continue
        
            