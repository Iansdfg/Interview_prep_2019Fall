class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        # write your code here
        base = n
        visited = set()
        while True:
            next_num = 0
            # print(base, next_num)
            while base:
                mod = base % 10
                next_num += mod ** 2
                base = base//10
                
            if next_num in visited:
                return False 
            visited.add(next_num)
            if next_num == 1:
                return True
            base = next_num
