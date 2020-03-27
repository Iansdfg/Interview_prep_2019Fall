class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        
        res = 0
        temp = x
        while temp:
            digit = temp % 10
            res += digit
            res *= 10
            temp //= 10
        return res//10 == x
        
            

        
