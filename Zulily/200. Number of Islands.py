from collections import deque
class Solution(object):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        island = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '0':
                    continue
                self.bfs(grid, row, col, visited)
                island += 1 
        return island
    
    def bfs(self, grid, row, col, visited):
        queue = deque([(row, col)])
        
        while queue:
            curr_x, curr_y = queue.popleft()
            visited.add((curr_x, curr_y))
            grid[curr_x][curr_y] = '0'
            for delta_x,delta_y in self.direction:
                next_x, next_y = curr_x + delta_x, curr_y + delta_y
                if self.is_valid(grid, next_x, next_y, visited):
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y))
                    
    def is_valid(self, grid, x, y, visited):
        rows = len(grid)
        cols = len(grid[0])
        if (x, y) in visited:
            return False 
        if x < 0 or x >= rows:
            return False
        if y < 0 or y >= cols:
            return False
        if grid[x][y] == '0':
            return False 
        return True 
        
        
        
        
        
                    
                    
                    
                    
                    
            
            
        
