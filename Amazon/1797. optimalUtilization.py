class Solution:
    """
    @param A: a integer sorted array
    @param B: a integer sorted array
    @param K: a integer
    @return: return a pair of index
    """
    def optimalUtilization(self, A, B, K):
        # write your code here
        if not A or not B or len(A) == 0 or len(B) == 0:
            return []
            
        a, b = 0, len(B) - 1 
        res = [-1, -1]
        curr_sum = 0
        while a<len(A) and b>=0:
            while b>=0 and A[a] + B[b]>K:
                if b == 0:
                    break
                b -= 1
            while b-1 >= 0 and B[b] == B[b-1]:
                b -= 1
                
            if A[a] + B[b] <= K:
                if A[a] + B[b] > curr_sum:
                    curr_sum = A[a] + B[b]
                    res = [a, b]
            a += 1 
        return res
