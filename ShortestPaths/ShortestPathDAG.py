class Graph:
    def __init__(self, V):
        self.adjList = [[] for _ in range(V)]
        self.inDegree = [0] * V
        self.V = V

    def addEdge(self,x,y,w):
        self.adjList[x].append((y, w))
        self.inDegree[y] += 1
    
    def topologicalSort(self):
        topOrder = []
        degZero = []
        # Find first vertex with in-degree 0
        for i in range(self.V):
            if (self.inDegree[i]==0):
                degZero.append(i)

        while (len(degZero) != 0):
            r = degZero.pop(0)
            topOrder.append(r)
            for u, w in self.adjList[r]:
                # Update degree of adjacent nodes
                self.inDegree[u] -= 1
                if (self.inDegree[u] == 0):
                    # Add to queue
                    degZero.append(u)
        if (len(topOrder) != self.V):
            print("Topological sorting failed. Not an directed acyclic graph!")
        return topOrder

    def shortestPath(self, start):
        order = self.topologicalSort()
        print(order)
        paths = [float('inf') for _ in range(self.V)]
        paths[start] = 0
        gor = False
        for v in order:
            if v == start:
                gor = True
            if gor:
                for u, w in self.adjList[v]:
                    if paths[u] > paths[v] + w:
                        paths[u] = paths[v] + w
        return paths

    def __str__(self) -> str:
        return str(self.adjList)

N = int(input())
M = int(input())

graph = Graph(N)
for _ in range(M):
    x, y, w = map(int, input().split())
    graph.addEdge(x, y, w)

print(graph.adjList)
print(graph.shortestPath(1))