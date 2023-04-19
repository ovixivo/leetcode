class Solution:
    def myAtoi(self, s: str) -> int:
        

        valid_key = '+-0123456789 '
        sign_num = '+-0123456789'
        num = '0123456789'
        s = s.lstrip()

        if len(s) == 0:
            return 0
        for i in range(len(s)):
            if s[i] in valid_key:
                s = s[i:]
                break
            else:
                return 0

        if s[0] not in sign_num or s[0] == ' ':
            return 0
        else:
            sign = 1
            if s[0] in '+-':
                if s[0] == '-':
                    sign = -1
                s = s[1:]

            ans_list = ['0']
            for i in range(len(s)):
                if s[i] in num:
                    ans_list.append(s[i])
                else:
                    break
            
            ans = int(''.join(ans_list)) * sign

            ans = max(ans, -2**31) 
            ans = min(ans, 2**31 - 1) 

        return ans