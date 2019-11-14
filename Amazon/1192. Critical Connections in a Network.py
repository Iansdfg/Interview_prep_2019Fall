from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        n = len(connections)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
        visited = [0]*n
        dfn = [float('inf')]*n
        low = [float('inf')]*n
        parent = [-1]*n
        count = 0
        
        result = []
        
        for i in range(n):
            if not visited[i]:
                self.get(i,graph,visited,dfn,low,parent,count,result)
        return result
    
    def get(self,u,graph,visited,disc,low,parent,time,result):

        visited[u]=True
        disc[u]=time
        low[u]=time
        time += 1

        for v in graph[u]:
            if visited[v]!=True:
                parent[v]=u

                self.get(v,graph,visited,disc,low,parent,time,result)

                low[u]=min(low[u],low[v])

                if low[v]>disc[u]:
                    result.append([u,v])

            elif v != parent[u]:
                low[u]=min(low[u],disc[v])
                
        
        
        
        
