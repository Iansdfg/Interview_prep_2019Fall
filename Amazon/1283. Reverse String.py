class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseString(self, s):
        # write your code here
        res = []
        for i in range(len(s)):
            res.append(s[len(s)-i-1])
        return ''.join(res)
