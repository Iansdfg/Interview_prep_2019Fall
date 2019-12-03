class Solution:
    """
    @param n: An integer
    @return: a square matrix
    """
    def generateMatrix(self, n):
        # write your code here
        if n == 0:
            return []
        matrix = [[0 for _ in range(n)]for _ in range(n)]
        
        up, down, left, right = 0, n-1, 0, n-1
        dirction, count = 0, 0
        
        while True:
            if dirction == 0:
                for i in range(left, right+1):
                    count += 1
                    matrix[up][i] = count
                up += 1
            if dirction == 1:
                for i in range(up, down+1):
                    count += 1
                    matrix[i][right] = count
                right -= 1
            if dirction == 2:
                for i in range(right, left-1, -1):
                    count += 1
                    matrix[down][i] = count
                down -= 1
            if dirction == 3:
                for i in range(down, up-1, -1):
                    count += 1
                    matrix[i][left] = count
                left += 1
            if count == n*n:
                return matrix
            dirction = (dirction + 1) % 4 
            
      
