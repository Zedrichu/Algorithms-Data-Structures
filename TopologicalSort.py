
class Graph:
    def __init__(self, V):
        self.adjList = [[] for _ in range(V)]
        self.inDegree = [0] * V
        self.V = V

    def add_edge(self,x,y):
        self.adjList[x].append(y)
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
            for u in self.adjList[r]:
                # Update degree of adjacent node
                self.inDegree[u] -= 1
                if (self.inDegree[u] == 0):
                    # Add to queue
                    degZero.append(u)
        if (len(topOrder) != self.V):
            print("Topological sorting failed. Not an directed acyclic graph!")
        return topOrder


    def __str__(self) -> str:
        return str(self.adjList)

N = int(input())
M = int(input())

graph = Graph(N)
for _ in range(M):
    x, y = map(int, input().split())
    graph.add_edge(x, y)

print(graph)
print(graph.topologicalSort())