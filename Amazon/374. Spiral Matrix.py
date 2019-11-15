class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        # write your code here
        if not len(matrix) or not len(matrix[0]):
            return []
        rows, cols = len(matrix), len(matrix[0])
        up, down, left, right = 0, rows-1, 0, cols-1
        dirction = 0
        res = []
        while True:
            if dirction == 0:
                for i in range(left, right+1):
                    res.append(matrix[up][i])
                up += 1
            if dirction == 1:
                for i in range(up, down+1):
                    res.append(matrix[i][right])
                right -= 1
            if dirction == 2:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if dirction == 3:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
            if up>down or left>right:
                return res
            dirction = (dirction+1)%4
                    
