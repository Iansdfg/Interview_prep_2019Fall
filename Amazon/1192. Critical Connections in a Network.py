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
            tarjan(node, node_to_children, visited, dfn,
            low, parent, count, result)
    return sorted(result)

def tarjan(curr, node_to_children, visited, dfn,
            low, parent, count, result):
    visited[curr] = 1
    dfn[curr] = count
    low[curr]= count
    count += 1
    
    for child in node_to_children[curr]:
        print(child)
        if not visited[child]:
            parent[child] = curr
            tarjan(child, node_to_children, visited, dfn,
                low, parent, count, result)
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
