class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        new = 0 
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            new = self.get_new(n)
            if new == 1:
                return True
            n = new 
            
    def get_new(self, num):
        res = 0
        while num:
            res += (num % 10)**2
            num //= 10
        return res
        
        
            
