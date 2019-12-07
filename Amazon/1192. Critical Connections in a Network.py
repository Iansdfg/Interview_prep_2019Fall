from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        curr_to_child = defaultdict(list)
        for x, y in connections:
            curr_to_child[x].append(y)
            curr_to_child[y].append(x)    
        visited = [0]*n
        order = [-1]*n
        low = [-1]*n
        parent = [-1]*n
        count = 1 
        result = []
        for node in range(n):
            self.targan(node, curr_to_child, visited, order, low, parent, count, result)
        return result
    
    
    
    def targan(self, curr, curr_to_child, visited, order, low, parent, count, result):
        visited[curr] = 1
        order[curr] = count
        low[curr] = count
        count += 1
        
        
        
        for child in curr_to_child[curr]:
            if not visited[child]:
                parent[child] = curr
                self.targan(child, curr_to_child, visited, order, low, parent, count, result)
                low[curr] = min(low[curr], low[child])
                
                if order[curr] < low[child]:
                    result.append([curr, child])
                    
            if parent[curr] != child:
                low[curr] = min(low[curr], order[child])
