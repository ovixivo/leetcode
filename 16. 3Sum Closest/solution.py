class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        s = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            prevSum = float('inf')
            prevDiff = float('inf')
            currDiff = 0
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                currDiff = abs(target - sum)
                if sum == target:
                    return sum
                elif sum > target:
                    k -= 1
                else:
                    j += 1

                prevDiff = min(prevDiff, currDiff)
                if prevDiff <= currDiff:
                    prevSum = sum
                    s.add(prevSum)
            if prevSum != float('inf'):
                s.add(prevSum)
        
        print(s)
        prevSum = float('inf')
        prevDiff = float('inf')
        currDiff = 0        
        for item in sorted(s):
            currDiff = abs(target - item)
            if prevDiff < currDiff:
                return prevSum
            prevDiff = currDiff
            prevSum = item
            
        return item