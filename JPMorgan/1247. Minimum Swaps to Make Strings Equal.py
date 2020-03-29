class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        n = len(s1)
        xy = 0
        yx = 0
        for i in range(n):
            if s1[i] == 'x' and s2[i] == 'y':
                xy += 1 
            if s1[i] == 'y' and s2[i] == 'x':
                yx += 1
        if (yx + xy) % 2:
            return -1
        return (xy + 1) // 2 + (yx + 1) // 2
        
