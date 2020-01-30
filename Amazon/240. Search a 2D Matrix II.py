class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix[0] == []:
            return False
        rows, cols = len(matrix), len(matrix[0])
        row, col = rows-1, 0
        while row >= 0 and col < cols:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True 
        return False
            
        
