class Solution(object):
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        word_list = self.words(num)
        res = ' '.join(word_list) if num else 'Zero'
        return res
    
    def words(self, n):
            if n < 20:
                return self.to19[n-1:n]
            if n < 100:
                return [self.tens[n/10-2]] + self.words(n%10)
            if n < 1000:
                return [self.to19[n/100-1]] + ['Hundred'] + self.words(n%100)
            if n < 1000**2:
                    return self.words(n/1000) + ['Thousand'] + self.words(n%1000)
            if n < 1000**3:
                    return self.words(n/1000**2) + ['Million'] + self.words(n%1000**2)
            if n < 1000**4:
                    return self.words(n/1000**3) + ['Billion'] + self.words(n%1000**3)
                
#             for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
#                 if n < 1000**(p+1):
#                     return self.words(n/1000**p) + [w] + self.words(n%1000**p)
                
                
                
                
                
                
                
