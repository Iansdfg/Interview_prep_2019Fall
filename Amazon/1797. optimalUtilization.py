class Solution:
    """
    @param A: a integer sorted array
    @param B: a integer sorted array
    @param K: a integer
    @return: return a pair of index
    """
    def optimalUtilization(self, A, B, K):
        # write your code here
        res = []
        max_sum = float('-inf')
        for pos_a, val_a in enumerate(A):
            for pos_b, val_b in enumerate(B):
                if val_a + val_b <= K:
            
                    summ = val_a + val_b
                    if summ > max_sum:
                        res = [pos_a, pos_b]
                    max_sum = max(summ, max_sum)

        return res
