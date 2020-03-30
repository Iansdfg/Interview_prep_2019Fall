class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        direction = 0
        result = []
        rows, cols = len(matrix), len(matrix[0])
        
        while len(result) < rows * cols:
            if direction == 0:
                for i in range(left, right + 1):
                    result.append(matrix[top][i])
                top += 1
            if direction == 1:
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1
            if direction == 2:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            if direction == 3:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
            # print(result, direction)
            direction = (direction + 1) % 4
        return result
            
            
