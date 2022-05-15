class UnionFind:
    
    def __init__(self,n):
        for i in range(n):
            self.p = [i for i in range(n)]
            self.sz = [1 for _ in range(n)]
        
    def find(self, x):
        if (x==self.p[x]):
            self.p[x] = self.find(self.p[x])
        return self.p[x] 
    
    def union(self, u, v):
        rU = self.find(u)
        rV = self.find(v)

        if rU != rV:
            if self.sz[rU] < self.sz[rV]:
                rU, rV = rV, rU
            self.p[rV] = rU
            self.sz[rU] += self.sz[rV]
    
    def connected(self, u, v):
        return self.find(u) == self.find(v)

N, M = list(map(int,input().split()))
edges = []

for _ in range(M):
    A, B, W = map(int,input().split())
    edges.append((A, B, W))

def Kruskal(edges):
    # Sort edges by weight
    edges.sort(key=lambda edge:edge[2])
    added = 0
    total_price = 0
    # Initialize the union find structure
    quick = UnionFind(N)

    # Iterate edges in sorted order
    for i in range(len(edges)):
        A, B, W = edges[i]

        # Edge does not create a cycle in tree
        if not quick.connected(A, B):
            # Add edge A->B to the tree
            quick.union(A, B)
            added += 1
            # Increase the total price of tree
            total_price += W
            # Tree has all vertices included
            if added == N-1:
                break

print(Kruskal(edges))