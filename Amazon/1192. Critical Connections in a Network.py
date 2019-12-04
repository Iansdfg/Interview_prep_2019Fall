from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        curr_to_children = defaultdict(list)
        for x, y in connections:
            curr_to_children[x].append(y)
            curr_to_children[y].append(x)
        visited = [0]*n
        order = [-1]*n
        low = [-1]*n
        father = [-1]*n
        res = []
        count = 0
        for node in range(n):
            self.tarjan(node, curr_to_children, visited, order, low, father, count, res)
        return res
        
    def tarjan(self, node, curr_to_children, visited, order, low, father, count, res):
        visited[node] = 1
        order[node] = count
        low[node] = count
        count += 1 
        
        for child in curr_to_children[node]:
            if not visited[child]:
                father[child] = node
                self.tarjan(child, curr_to_children, visited, order, low, father, count, res)
                low[node] = min(low[node], low[child])

                if order[node] < low[child]:
                    res.append([node, child])
                
            if child != father[node]:
                low[node] = min(low[node], order[child])
            
            
            
            
            
            
            
            
