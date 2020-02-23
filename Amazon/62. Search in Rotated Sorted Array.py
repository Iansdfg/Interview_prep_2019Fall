class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if len(A) == 0:
            return -1
        left, right = 0, len(A) - 1 
        while left + 1 < right:
            mid = (left + right) // 2 
            
            if A[mid] < A[right]:
                if A[mid] <= target <= A[right]:
                    left = mid 
                else:
                    right = mid 
            else:
                if A[left] <= target <= A[mid]:
                    right = mid 
                else:
                    left = mid 
                    
        if A[left] == target:
            return left
        if A[right] == target:
            return right 
        return -1