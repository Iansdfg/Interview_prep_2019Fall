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
                self.tarjan(i,graph,visited,dfn,low,parent,count,result)
        return result
    
    def tarjan(self,curr,graph,visited,dfn,low,parent,count,result):

        visited[curr]=True
        dfn[curr]=count
        low[curr]=count
        count += 1

        for child in graph[curr]:
            if visited[child]!=True:
                parent[child]=curr

                self.tarjan(child,graph,visited,dfn,low,parent,count,result)

                low[curr]=min(low[curr],low[child])

                if low[child]>dfn[curr]:
                    result.append([curr,child])
                    
                # find critical point
                # if low[child]>=dfn[curr]:
                #     result.append(curr)

            if child != parent[curr]:
                low[curr]=min(low[curr],dfn[child])
                
        
        
        
        
