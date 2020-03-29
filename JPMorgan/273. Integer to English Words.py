class Solution(object):
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        return ' '.join(self.words(num)) or 'Zero'
    
    def words(self, n):
            if n < 20:
                return self.to19[n-1:n]
            if n < 100:
                return [self.tens[n/10-2]] + self.words(n%10)
            if n < 1000:
                return [self.to19[n/100-1]] + ['Hundred'] + self.words(n%100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000**(p+1):
                    return self.words(n/1000**p) + [w] + self.words(n%1000**p)
