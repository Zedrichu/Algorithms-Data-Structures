class WeightedUnion:
    
    def __init__(self, N):
        self.sz = [1 for _ in range(N)]
        self.p = [i for i in range(N)]
    
    def findPath(self, i):
        if (i != self.p[i]):
            self.p[i] = self.findPath(self.p[i])
        return self.p[i]
    
    def union(self,i,j):
        ri = self.findPath(i)
        rj = self.findPath(j)
        if (ri != rj):
            if (self.sz[ri] < self.sz[rj]):
                self.p[ri] = rj
                self.sz[rj] += self.sz[ri]
            else:
                self.p[rj] = ri
                self.sz[ri] += self.sz[rj]


N = int(input())
M = int(input())
lines = [input().split() for _ in range(M)]
WU = WeightedUnion(N)
for line in lines:
    if line[0]=='F':
        print(WU.findPath(int(line[1])))
    elif line[0]=='U':
        WU.union(int(line[1]),int(line[2]))
