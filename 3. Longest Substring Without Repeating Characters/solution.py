class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        char_set = set()

        answer = 0
        l = 0

        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[i])
            answer = max(answer, i - l + 1)
        
        return answer
