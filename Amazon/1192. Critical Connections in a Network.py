# O(e*(v+e))
from collections import defaultdict
from collections import deque
class Solution:
    def criticalConnections_brutal(self, n, connections):
        result = []
        
        for edge in connections:
            new_connections = connections[:]
            new_connections.remove(edge)
            graph_list = self.construct_graph(new_connections)
            connected = self.check_connection(graph_list, n)
            if not connected:
                result.append(edge)

        return result
        
    def construct_graph(self, connections):
#         return adjacent list 
        node_to_children = defaultdict(list)
        for x, y in connections:
            node_to_children[x].append(y)
            node_to_children[y].append(x)
        return node_to_children
    
    def check_connection(self, graph_list, n):
        # return True or False
        if len(graph_list) != n: 
            return False
        visited = set()
        q = deque([0])
        while q:
            curr = q.popleft()
            visited.add(curr)
            for node in graph_list[curr]:
                if node not in visited:
                    visited.add(node)
                    q.append(node)

        return len(visited) == n



        
    def criticalConnections(self, n: int, connections):
        node_to_children = defaultdict(list)
        for x,y in connections:
            node_to_children[x].append(y)
            node_to_children[y].append(x)
        visited = [0]*n
        order = [0]*n
        low = [0]*n
        parent = [-1]*n
        count = 0
        result = []
        
        for node in range(n):
            if not visited[node]:
                self.targan(node, node_to_children, visited, order, low, parent, count, result)
            
        # result.sort(key =lambda x:x[1])
        return sorted(result, key =lambda x:x[1])
        
        
    def targan(self, node, node_to_children, visited, order, low, parent, count, result):
        visited[node] = 1
        order[node] = count
        low[node] = count
        count += 1
        
        for child in node_to_children[node]:
            if not visited[child]:
                parent[child] = node
                self.targan(child, node_to_children, visited, order, low, parent, count, result)
                low[node] = min(low[node], low[child])
                
                if order[node]<low[child]:
                    fomer, later = min(node, child), max(node, child)
                    result.append([fomer, later])
                    
            if parent[node] != child:
                low[node] = min(low[node], order[child])

# O(v+e)

from collections import defaultdict

def criticalConnection(numOfWarehouses, numOfRoads, roads):
    # WRITE YOUR CODE HERE
    node_to_children = defaultdict(list)
    n = numOfWarehouses+1
    for x, y in roads:
        node_to_children[x].append(y)
        node_to_children[y].append(x)
    print(node_to_children)
    visited = [0]*n
    dfn = [float('inf')]*n
    low = [float('inf')]*n
    parent = [-1]*n
    count = 0 
    result = []
    for node in range(n):
        if not visited[node]:
            tarjan(node, node_to_children, visited, dfn, low, parent, count, result)
    return sorted(result)

def tarjan(curr, node_to_children, visited, dfn, low, parent, count, result):
    visited[curr] = 1
    dfn[curr] = count
    low[curr]= count
    count += 1
    
    for child in node_to_children[curr]:
        print(child)
        if not visited[child]:
            parent[child] = curr
            tarjan(child, node_to_children, visited, dfn, low, parent, count, result)
            low[curr] = min(low[curr], low[child])
            
            if low[child] > dfn[curr]:
                former, later= min(curr, child), max(curr, child)
                result.append([former, later])

        if child != parent[curr]:
            low[curr] = min(low[curr], dfn[child])
            
    
numOfWarehouses = 6
numOfRoads = 5
roads = [[1,2], [2,3], [3,4], [4,5], [6,3]]
res = criticalConnection(numOfWarehouses, numOfRoads, roads )
print(res)


