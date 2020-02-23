class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if len(s) == 1:
            return s
        max_sub = ''
        
        for i in range(1, len(s)):
            palindrome = self.find_palindrome(s, i, i - 1)
            if len(palindrome) > len(max_sub):
                max_sub = palindrome
                
            palindrome = self.find_palindrome(s, i, i)
            if len(palindrome) > len(max_sub):
                max_sub = palindrome
                
        return max_sub
            
            
    def find_palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1 
            r += 1
        # print(l,r)
        return s[l+1:r]
