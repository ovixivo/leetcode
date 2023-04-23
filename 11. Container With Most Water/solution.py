class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = 0
        m = len(height) - 1

        area = 0
        while n != m:
            shortest = min(height[n], height[m])
            area = max(area, shortest * (m-n))
            if height[m] < height[n]:
                m -= 1
            else:
                n += 1
        
        return area