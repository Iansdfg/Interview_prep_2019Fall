from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        visited = set()
        orange_num = self.find_all_rotten(grid, queue, visited)
        if orange_num == 0:
            return 0
        days = self.bfs(grid, queue, visited)
        return days - 1 if orange_num == len(visited) else -1 
    
    def find_all_rotten(self, grid, queue, visited):
        orange_num = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    orange_num += 1
                if grid[row][col] == 2:
                    orange_num += 1
                    queue.append((row, col))
                    visited.add((row, col))
        return orange_num
        
    def bfs(self, grid, queue, visited):
        day = 0
        while queue:
            day += 1
            for _ in range(len(queue)):
                curr_x, curr_y  = queue.popleft()
                visited.add((curr_x, curr_y))
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for detla_x, detla_y in directions:
                    next_x, next_y = curr_x + detla_x, curr_y + detla_y
                    if self.is_valid(next_x, next_y, visited, grid):
                        queue.append((next_x, next_y))
                        visited.add((next_x, next_y))
        return day          
                        
    def is_valid(self, x, y, visited, grid):
        if (x, y) in visited:
            return False
        if x < 0 or x >= len(grid):
            return False 
        if y < 0 or y >= len(grid[0]):
            return False 
        if grid[x][y] != 1:
            return False 
        return True
    
        
        
        
        
        

            
