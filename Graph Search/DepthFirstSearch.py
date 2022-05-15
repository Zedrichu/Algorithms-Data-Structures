class Graph:
    def __init__(self, V):
        self.adjList = [[] for _ in range(V)]
        self.V  = V
        self.initial = [0 for _ in range(V)]
        self.final = [0 for _ in range(V)]
        self.time = 0
        self.visited = [False for _ in range(V)]
        self.parent = [i for i in range(V)]
        self.order = []

    def addEdge(self, x, y):
        self.adjList[x].append(y)
    
    def DFS(self, v):
        # Start processing of vertex
        self.initial[v] = self.time
        self.time += 1
        
        # Mark vertex as visited
        self.visited[v] = True
        self.order.append(v)

        # Continue with adjacent vertices
        for u in self.adjList[v]:
            if not self.visited[u]:
                self.parent[u] = v
                self.DFS(u)

        # Finish the processing of vertex
        self.final[v] = self.time
        self.time += 1

    def __str__(self) -> str:
        return str(self.adjList)

N = int(input())
M = int(input())

graph = Graph(N)
for _ in range(M):
    x, y = map(int, input().split())
    graph.addEdge(x, y)

graph.DFS(0)
print(graph.order)
print(graph.initial)
print(graph.final)

