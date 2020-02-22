class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for layer in range(n//2):
            first = layer
            last = n - 1 - layer
            for i in range(first, last):
                dis = i - first
                temp = matrix[first][i]
                matrix[first][i] = matrix[last - dis][first]
                matrix[last - dis][first] = matrix[last][last - dis]
                matrix[last][last - dis] = matrix[i][last]
                matrix[i][last] = temp
                
    
