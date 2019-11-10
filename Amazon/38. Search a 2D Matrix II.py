class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        rows, cols = len(matrix), len(matrix[0])
        if rows ==0 or cols == 0:
            return 0
        
        row, col = rows-1, 0
        count = 0
        while row >= 0 and col < cols:
            if matrix[row][col] == target:
                row -= 1
                col += 1
                count += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                col += 1

        return count
                
