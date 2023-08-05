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

    def shortestPath(self, start): # O(N+M)
        # Compute the topological order used for processing
        order = self.topologicalSort()
        print("Sequence of vertices in topple:"+str(order))
        # Initialize path distance estimates for every vertex
        paths = [float('inf') for _ in range(self.V)]
        paths[start] = 0
        gor = False
        for v in order:
            # Wait for the start node to occur in topological sort
            if v == start:
                gor = True
            if gor:
                # Relax all the incident edges
                for u, w in self.adjList[v]:
                    # Distance estimate can be decreased
                    if paths[u] > paths[v] + w:
                        paths[u] = paths[v] + w
        return paths

    def longestPath(self, start): # O(N+M)
        # Compute the topological order used for processing
        order = self.topologicalSort()
        print("Sequence of vertices in topple:"+str(order))
        # Initialize path distance estimates for every vertex
        paths = [float('-inf') for _ in range(self.V)]
        paths[start] = 0
        gor = False
        for v in order:
            # Wait for the start node to occur in topological sort
            if v == start:
                gor = True
            if gor:
                # Stress all the incident edges
                for u, w in self.adjList[v]:
                    # Distance estimate can be increased
                    if paths[u] < paths[v] + w:
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

print("Graph edges:"+str(graph.adjList))
print("Shortest path for topple sequence:"+str(graph.shortestPath(1)))
print("Longest path for topple sequence:"+str(graph.longestPath(1)))