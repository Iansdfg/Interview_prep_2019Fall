class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        # write your code here
        visited = set()
        temp = n
        while True:
            temp = self.happify(temp)
            if temp in visited:
                return False
            if temp == 1:
                return True
            visited.add(temp)

        
    def happify(self, n):
        summ = 0
        while n:
            summ += (n%10)**2
            n//=10
        return summ
        
