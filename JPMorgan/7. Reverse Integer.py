class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos = 1 if x > 0 else 0
        x = abs(x)
        res = 0
        while x:
            res *= 10
            res += x % 10
            x //= 10
        if res > 2**31 - 1:
            return 0
        return res if pos else res*-1
        
        
