class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        sorted_strs = sorted(strs)

        first_item = sorted_strs[0]
        last_item = sorted_strs[-1]

        ans = ''
        for i in range(min(len(first_item), len(last_item))):
            if first_item[i] == last_item[i]:
                ans+= first_item[i]
            else:
                break
        return ans
