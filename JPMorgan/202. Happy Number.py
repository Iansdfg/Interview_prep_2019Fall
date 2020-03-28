class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set([n])
        while n != 1:
            new = self.get_new(n)
            if new in visited:
                return False
            visited.add(new)
            n = new 
        return True
            
    def get_new(self, n):
        res = 0
        while n:
            res += (n % 10)**2
            n //= 10
        return res
