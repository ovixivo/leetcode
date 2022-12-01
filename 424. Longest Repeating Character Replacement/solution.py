class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = defaultdict(lambda: 0)
        leftIdx = 0
        maxLen = 0
        for rightIdx in range(len(s)):
            
            freq[s[rightIdx]] += 1
            
            currLen = rightIdx - leftIdx + 1
            
            if currLen - max(freq.values()) <= k:
                maxLen = max(currLen, maxLen)
            else:
                freq[s[leftIdx]] -= 1
                leftIdx += 1
                
        return maxLen