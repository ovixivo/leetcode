class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

#        if str(x)[::-1] == str(x):
#            return True

        rev = 0
        orig = x
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10

        return orig == rev