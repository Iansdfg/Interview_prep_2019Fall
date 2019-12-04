from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        curr_to_children = defaultdict(list)
        n = len(connections)
        for x,y in connections:
            curr_to_children[x].append(y)
            curr_to_children[y].append(x)
        visited = [0]*n
        dfn = [float('inf')]*n
        low = [float('inf')]*n
        parent = [-1]*n
        count = 0
        result = []
        for node in range(n):
            if not visited[node]:
                self.tarjan(node, curr_to_children, visited, dfn, low, parent, count, result)
        return result
                
    def tarjan(self, curr, curr_to_children, visited, dfn, low, parent, count, result):
        visited[curr] = 1
        dfn[curr] = count
        low[curr] = count
        count += 1
        
        for child in curr_to_children[curr]:
            if not visited[child]:
                parent[child] = curr
                self.tarjan(child, curr_to_children, visited, dfn, low, parent, count, result)
                low[curr] = min(low[curr], low[child])
                
                if low[child] > dfn[curr]:
                    result.append([curr, child])
            if child != parent[curr]:
                low[curr] = min(low[curr], dfn[child])
                    
                
